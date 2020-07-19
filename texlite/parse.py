from texlite.components import Meta, DocumentBegin, DocumentEnd, MakeTitle, Section, Text


def parse(md_lines):

    # set up initial components
    meta = Meta()
    components = [
        DocumentBegin(),
    ]

    # parse lines
    i, n_lines = 0, len(md_lines)
    while i < n_lines:

        # read in line
        line = md_lines[i]
        prefix = line.split(' ')[0]
        body = ' '.join(line.split(' ')[1:])

        # handle optional meta prefixes
        if prefix == 'title:':
            meta.title = body
        elif prefix == 'author:':
            meta.author = body
        elif prefix == 'date:':
            meta.date = body

        # handle component prefixes
        elif prefix == '#':
            components.append(Section(body, section_type='section'))
        elif prefix == '##':
            components.append(Section(body, section_type='subsection'))
        elif prefix == '###':
            components.append(Section(body, section_type='subsubsection'))
        else:
            components.append(Text(line))

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
