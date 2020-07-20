import argparse
from pathlib import Path

from texlite.io import read_md_lines, write_tex_lines
from texlite.parse import parse
from texlite.compile import compile_tex_to_pdf


def validate_source_file(source_path):

    # check if file exists
    if not source_path.exists():
        return False, f'Error: The file "{source_path}" could not be found.'

    # check if file is markdown
    if not source_path.suffix == '.md':
        return False, 'Error: Source file must be in markdown (.md) format.'

    return True, None


if __name__ == '__main__':

    # parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=str,
                        help='path to source markdown (.md) file to parse and compile')
    parser.add_argument('--save-tex', action='store_true', default=False,
                        help='save TeX (.tex) file used in compilation')
    parser.add_argument('--show-tex-output', action='store_true', default=False,
                        help='show output for TeX and pdfLaTeX processes')
    args = parser.parse_args()

    # check source file
    source_path = Path(args.source)
    is_valid, error = validate_source_file(source_path)
    if not is_valid:
        print(error)
        exit()

    # get base path
    base_path = source_path.parents[0] / source_path.stem

    # read in markdown lines from file
    md_path = base_path.with_suffix('.md')
    md_lines = read_md_lines(path=md_path)

    # translate markdown to tex
    tex_lines = parse(md_lines)

    # write out tex lines to file
    tex_path = base_path.with_suffix('.tex')
    write_tex_lines(path=tex_path, lines=tex_lines)

    # compile to pdf
    compile_tex_to_pdf(path=tex_path, save_tex=args.save_tex,
                       show_tex_output=args.show_tex_output)
