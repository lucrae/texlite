from pathlib import Path

from texlite.io import read_md_lines, write_tex_lines
from texlite.parse import parse
from texlite.compile import compile_tex_to_pdf


if __name__ == '__main__':

    filename = 'example'

    # read in markdown lines from file
    md_file_path = Path(f'{filename}.md')
    md_lines = read_md_lines(file_path=md_file_path)

    # translate markdown to tex
    tex_lines = parse(md_lines)

    # write out tex lines to file
    tex_file_path = Path(f'{filename}.tex')
    write_tex_lines(tex_lines, file_path=tex_file_path)

    # compile to pdf
    compile_tex_to_pdf(tex_file_path=tex_file_path, keep_tex=True, verbose=True)