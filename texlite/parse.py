from texlite.components import (
    Meta, DocumentBegin, DocumentEnd, MakeTitle, Section, Text,
    UnorderedList, OrderedList
)


# useful constants and string sets
UNORDERED_LIST_PREFIXES = r'-+*'
NUMBERS = '0123456789'
LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def parse(md_lines):

    # set up meta object and initial components
    meta = Meta()
    components = [
        DocumentBegin(),
    ]

    # parse lines
    i, n_lines = 0, len(md_lines)
    while i < n_lines:

        # read in line elements
        prefix = get_line_prefix(md_lines[i])
        body = get_line_without_prefix(md_lines[i])

        # handle optional meta specifications
        if prefix == 'title:':
            meta.title = body
        elif prefix == 'author:':
            meta.author = body
        elif prefix == 'date:':
            meta.date = body
        elif prefix == 'fontsize:':
            meta.fontsize = body
        elif prefix == 'margin:':
            meta.margin = body

        # handle heading/section
        elif prefix == '#':
            components.append(Section(body, section_type='section'))
        elif prefix == '##':
            components.append(Section(body, section_type='subsection'))
        elif prefix == '###':
            components.append(Section(body, section_type='subsubsection'))
        elif prefix == '#*':
            components.append(Section(body, section_type='section*'))
        elif prefix == '##*':
            components.append(Section(body, section_type='subsection*'))
        elif prefix == '###*':
            components.append(Section(body, section_type='subsubsection*'))

        # handle unordered list
        elif prefix in UNORDERED_LIST_PREFIXES and not is_empty(prefix):
            # XXX: the not is_empty condition prevents tabbed lines from
            # being interpreted as items in an ordered list, but I really
            # don't know why it even does that in the first place

            items = []
            while i < n_lines:

                # break if line is not item
                if get_line_prefix(md_lines[i]) not in UNORDERED_LIST_PREFIXES:
                    
                    # decrement index to counter end-of-loop increment and break
                    i -= 1
                    break

                # add line to items
                items.append(get_line_without_prefix(md_lines[i]))
                i += 1

            components.append(UnorderedList(items))

        # handle ordered list
        elif prefix in [f'{n}.' for n in NUMBERS]:

            items = []
            while i < n_lines:

                # break if line is not item
                if get_line_prefix(md_lines[i]) not in [f'{n}.' for n in NUMBERS]:
                    
                    # decrement index to counter end-of-loop increment and break
                    i -= 1
                    break

                # add line to items
                items.append(get_line_without_prefix(md_lines[i]))
                i += 1

            components.append(OrderedList(items))

        # handle comment
        elif prefix == '<!--':

            # iterate through lines until a '-->' is reached
            while i < n_lines:
                if '-->' in md_lines[i]:
                    break
                i += 1

        # interpret as text content
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

    # convert components to lines
    tex_lines = [component.tex() + '\n' for component in components]
    return tex_lines


def get_line_prefix(line):
    return line.split(' ')[0]


def get_line_without_prefix(line):
    return ' '.join(line.split(' ')[1:])


def is_empty(text):
    return bytes(text, encoding='utf-8') == b''