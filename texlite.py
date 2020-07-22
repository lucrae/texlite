import argparse
from pathlib import Path

from texlite.io import read_md_lines, write_tex_lines
from texlite.parse import parse
from texlite.compile import compile_tex_to_pdf
from texlite.messages import message, error


def _check_source(source_path):
    '''Checks input source and halts on error'''

    # check if file exists
    if not source_path.exists():
        error(f'Source file "{source_path}" could not be found')

    # check if file is markdown
    if not source_path.suffix == '.md':
        error('Source file must be in markdown (.md) format')


if __name__ == '__main__':

    # parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=str,
                        help='path to source markdown (.md) file to parse and '
                        'compile')
    parser.add_argument('--save-tex', action='store_true', default=False,
                        help='save TeX (.tex) file used in compilation')
    parser.add_argument('--show-tex-output', action='store_true',
                        default=False, help='show output for TeX and pdfLaTeX '
                        'processes')
    parser.add_argument('--open-with', metavar='PROGRAM',
                        help='open PDF upon compilation with a given document '
                        'viewer')
    args = parser.parse_args()

    # form source path (and add .md if no suffix given)
    source_path = Path(args.source)
    if source_path.suffix == '':
        source_path = source_path.with_suffix('.md')

    # check source path
    _check_source(source_path)
    message(f'Reading in "{source_path}"...')

    # get directory path and base path (stem of files)
    dir_path = source_path.parents[0]
    base_path = dir_path / source_path.stem

    # read in markdown lines from file
    md_path = base_path.with_suffix('.md')
    md_lines = read_md_lines(path=md_path)

    # translate markdown to tex
    tex_lines = parse(md_lines, graphics_path=dir_path)

    # write out tex lines to file
    tex_path = base_path.with_suffix('.tex')
    write_tex_lines(path=tex_path, lines=tex_lines)

    # compile to pdf
    compile_tex_to_pdf(path=tex_path,
                       save_tex=args.save_tex,
                       show_tex_output=args.show_tex_output,
                       open_with=args.open_with)
