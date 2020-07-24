import re

from texlite.components import (
    Meta, DocumentBegin, DocumentEnd, MakeTitle, Section, Text,
    UnorderedList, OrderedList, Figure, Equation
)


# set useful constants and string sets
NUMBERS = '0123456789'
LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
UNORDERED_LIST_PREFIXES = ['-', '+', '*']
ORDERED_LIST_PREFIXES = [f'{n}.' for n in NUMBERS]

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


def parse(md_lines, graphics_path=None):

    # set up meta object and initial components
    meta = Meta(graphics_path=graphics_path)
    components = [
        DocumentBegin(),
    ]

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
            # XXX: Will not handle nested lists (lists within lists)

            items = []
            while i < n_lines:

                # break if line is not item
                if get_line_prefix(md_lines[i]) not in UNORDERED_LIST_PREFIXES:

                    # go back to align with end-of-loop increment and break
                    i -= 1
                    break

                # add line to items
                items.append(get_line_without_prefix(md_lines[i]))
                i += 1

            # add unordered list component
            components.append(UnorderedList(items))

        # handle ordered list
        elif prefix in ORDERED_LIST_PREFIXES:
            # XXX: Will not handle nested lists (lists within lists)

            items = []
            while i < n_lines:

                # break if line is not item
                if get_line_prefix(md_lines[i]) not in ORDERED_LIST_PREFIXES:

                    # go back to align with end-of-loop increment and break
                    i -= 1
                    break

                # add line to items
                items.append(get_line_without_prefix(md_lines[i]))
                i += 1

            # add ordered list component
            components.append(OrderedList(items))

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
    if meta.title:
        components.insert(2, MakeTitle())

    # convert tokenised components to lines
    tex_lines = [component.tex() + '\n' for component in components]
    return tex_lines


def get_line_prefix(line):
    return line.split(' ')[0]


def get_line_without_prefix(line):
    return ' '.join(line.split(' ')[1:])


def is_empty(text):
    return bytes(text, encoding='utf-8') == b''
