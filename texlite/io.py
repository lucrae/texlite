def read_md_lines(file_path):

    # create list of markdown file lines
    lines = []
    with open(f'{file_path}', 'r', encoding='utf-8') as f:
        for i, raw_line in enumerate(f.readlines()):

            # remove newline markers
            line = raw_line.strip('\n')

            if line:

                # append (non-empty) line
                lines.append(line)

    return lines


def write_tex_lines(lines, file_path):

    # write tex lines in file
    with open(f'{file_path}', 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(f'{line}\n')