
def md_to_tex(md_line):

    tex = md_line

    if md_line.startswith('#'):

        content = ' '.join(md_line.split(' ')[1:])

        tex = '\section{' + content + '}'

    return tex


filename = 'example2'
lines = []

with open(f'{filename}.md', 'r', encoding='utf-8') as f:
    for i, raw_line in enumerate(f.readlines()):

        # strip newline and append
        line = raw_line.strip('\n')
        lines.append(line)

with open(f'{filename}.tex', 'w', encoding='utf-8') as f:
    
    # write start
    start = [
        r'\documentclass{article}',
        '',
        r'% ------------------------------------------------------------',
        r'% packages',
        r'% ------------------------------------------------------------',
        '',
        r'\usepackage[utf8]{inputenc}',
        '',
        r'% ------------------------------------------------------------',
        r'% document details',
        r'% ------------------------------------------------------------',
        '',
        r'\title{Hello, World!}',
        r'\author{Author McAuthorFace}',
        r'\date{July 2020}',
        '',
        r'% ------------------------------------------------------------',
        r'% document content',
        r'% ------------------------------------------------------------',
        '',
        r'\begin{document}',
        '',
        r'\maketitle',
        '',
    ]

    # write start lines
    for line in start:
        f.write(f'{line}\n')

    # write main lines
    for line in lines:
        f.write(f'{md_to_tex(line)}\n')

    # write end
    end = [
        '',
        r'\end{document}'
    ]

    # write end lines
    for line in end:
        f.write(f'{line}\n')