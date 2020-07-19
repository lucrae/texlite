from pathlib import Path

from texlite.io import read_md_lines, write_tex_lines
from texlite.parse import parse
from texlite.compile import compile_tex_to_pdf


if __name__ == '__main__':

    file_path = Path('examples', 'basic') # examples/basic.md

    # read in markdown lines from file
    md_path = file_path.with_suffix('.md')
    md_lines = read_md_lines(path=md_path)

    # translate markdown to tex
    tex_lines = parse(md_lines)

    # write out tex lines to file
    tex_path = file_path.with_suffix('.tex')
    write_tex_lines(path=tex_path, lines=tex_lines)

    # compile to pdf
    compile_tex_to_pdf(path=tex_path, verbose=True)