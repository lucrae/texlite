import re
from pathlib import Path
from typing import List as L

from texlite.components import (
    Meta, DocumentBegin, DocumentEnd, MakeTitle, Section, Text,
    List, Figure, Equation
)


# set useful constants and string sets
NUMBERS = '0123456789'
LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
UNORDERED_LIST_PREFIXES = ['-', '+', '*']
ORDERED_LIST_PREFIXES = [f'{c}.' for c in NUMBERS + LETTERS]
LIST_PREFIXES = UNORDERED_LIST_PREFIXES + ORDERED_LIST_PREFIXES
TAB = r' ' * 4 # tabs are four spaces

# set section heading codes
HEADINGS = {
    '#': 'section',
    '##': 'subsection',
    '###': 'subsubsection',
    '#*': 'section',
    '##*': 'subsection',
    '###*': 'subsubsection',
}

# regex patterns
FIGURE_RE = re.compile(r'^(!\[.*\]\(.*\))$')


def parse(md_lines: L[str], graphics_path: Path=None,
          package_config_path: Path=None) -> L[str]:
    '''Parses list of Markdown (.md) lines and returns TeX (.tex) lines'''

    # set up meta object and initial components
    meta = Meta(
        graphics_path=graphics_path,
        package_config_path=package_config_path
    )
    components = [DocumentBegin()]

    # iteratively tokenise lines
    i, n_lines = 0, len(md_lines)
    while i < n_lines:

        # read in line elements
        prefix = get_line_prefix(md_lines[i])
        body = get_line_without_prefix(md_lines[i])

        # handle optional meta specifications
        if prefix in [f':{option}:' for option in meta.options]:

            # set meta attribute to specified value
            option_name = prefix[1:-1]
            setattr(meta, option_name, body)

        # handle heading/section
        elif prefix in HEADINGS.keys():

            # add section (heading) component
            components.append(Section(body, section_type=HEADINGS[prefix]))

        # handle unordered list
        elif prefix in UNORDERED_LIST_PREFIXES:

            # parse list and add list component
            list_component, i = _parse_list(i, md_lines, ordered=False)
            components.append(list_component)

        # handle ordered list
        elif prefix in ORDERED_LIST_PREFIXES:

            # parse list and add list component
            list_component, i = _parse_list(i, md_lines, ordered=True)
            components.append(list_component)

        # handle figures
        elif FIGURE_RE.match(md_lines[i]):

            # get details of figure component
            image_path = re.findall(r'\((.*)\)', md_lines[i])[0]
            caption_text = re.findall(r'\[(.*)\]', md_lines[i])[0]

            # add figure component
            components.append(Figure(graphics_path, image_path, caption_text))

        # handle equation
        elif prefix == '$$$':

            # skip to next line and then iterate through until $$$ is reached
            equation_lines = []
            i += 1
            while i < n_lines:

                # break out at end
                if md_lines[i] == '$$$':
                    break

                equation_lines.append(md_lines[i])

                i += 1

            components.append(Equation(equation_lines))

        # handle comment
        elif prefix == '<!--':

            # iterate through lines until a '-->' is reached
            while i < n_lines:
                if '-->' in md_lines[i]:
                    break
                i += 1

        # interpret as text content (by default)
        else:
            components.append(Text(md_lines[i]))

        # increment to next line
        i += 1

    # append document end and add meta to start
    components.append(DocumentEnd())
    components.insert(0, meta)

    # add maketitle if needed
    if meta.title or meta.abstract:
        components.insert(2, MakeTitle(meta))

    # convert tokenised components to lines
    tex_lines = [component.tex() + '\n' for component in components]
    return tex_lines


def _parse_list(i: int, md_lines: L[str], ordered: bool=False,
                depth: int=0) -> List:
    '''Parse Markdown lines containing a list and return List component'''

    # NOTE: Nested lists must be done with four-space indentation

    # set prefixes
    prefixes = ORDERED_LIST_PREFIXES if ordered else UNORDERED_LIST_PREFIXES

    # iterate through lines
    items = []
    while i < len(md_lines):

        # get line without tabs (at specific depth)
        line_without_tab = md_lines[i][depth * len(TAB):]

        # read in line if at proper depth
        if get_line_prefix(line_without_tab) in prefixes:

            # add line to items
            items.append(get_line_without_prefix(line_without_tab))
            i += 1

        # if tabbed inwards, create nested list (NOTE: recursive)
        elif (TAB * (depth + 1) in md_lines[i] and
                get_line_prefix(md_lines[i].lstrip()) in LIST_PREFIXES):

            # determine if nested list
            if get_line_prefix(md_lines[i].lstrip()) in ORDERED_LIST_PREFIXES:
                nested_ordered = True
            else:
                nested_ordered = False

            # parse nested list and append
            list_component, i = _parse_list(i, md_lines,
                                            ordered=nested_ordered,
                                            depth=depth + 1)
            items.append(list_component)
            i += 1

        # exit out of list
        else:

            # go back to align with end-of-loop increment and break
            i -= 1
            break

    # return list object and ending line for parsing to be picked up from
    return List(items, ordered=ordered), i


def get_line_prefix(line: str) -> str:
    '''Returns first section of a line'''

    return line.split(' ')[0]


def get_line_without_prefix(line: str) -> str:
    '''Returns line without first section'''

    return ' '.join(line.split(' ')[1:])


def is_empty(text: str) -> bool:
    '''Returns true if the given string is completely empty'''

    return bytes(text, encoding='utf-8') == b''
