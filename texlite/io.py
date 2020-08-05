from pathlib import Path


def read_md_lines(path: Path) -> list:
    '''Returns a stripped list from the lines of a given Markdown (.md) file'''

    # create list of markdown file lines
    lines = []
    with open(path, 'r', encoding='utf-8') as f:
        for i, raw_line in enumerate(f.readlines()):

            # remove newline markers
            line = raw_line.strip('\n')

            if line:

                # append (non-empty) line
                lines.append(line)

    return lines


def write_tex_lines(path: Path, lines: list) -> None:
    '''Writes out a TeX (.tex) file given a list of the file lines'''

    # write tex lines in file
    with open(path, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(f'{line}\n')
