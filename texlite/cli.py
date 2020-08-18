from pathlib import Path
from argparse import Namespace

from texlite import messages as msg
from texlite.io import read_md_lines, write_tex_lines
from texlite.parse import parse
from texlite.compile import compile_tex_to_pdf


def _check_source(source_path: Path) -> (bool, str):
    '''Checks existence and file type of inputted source path'''

    # check if file exists
    if not source_path.exists():
        return False, f'Source file \'{source_path}\' not found'

    # check if file is markdown
    if not source_path.suffix == '.md':
        return False, 'Source file must be in markdown (.md) format'

    # return success and message
    return True, f'Reading in document \'{source_path}\'...'


def run(args: Namespace) -> bool:
    '''Runs main program cycle'''

    # form source path (and add .md if no suffix given)
    source_path = Path(args.source)
    if source_path.suffix == '':
        source_path = source_path.with_suffix('.md')

    # check source path
    source_success, source_message = _check_source(source_path)

    # display source success
    if source_success:
        msg.message(source_message)
    else:
        msg.error(source_message)
        return False

    # get directory path and base path (stem of files)
    dir_path = source_path.parents[0]
    base_path = dir_path / source_path.stem

    # read in markdown lines from file
    md_path = base_path.with_suffix('.md')
    md_lines = read_md_lines(path=md_path)

    # translate markdown to tex
    tex_lines = parse(md_lines,
                      graphics_path=dir_path,
                      package_config_path=args.default_packages)

    # write out tex lines to file
    tex_path = base_path.with_suffix('.tex')
    write_tex_lines(path=tex_path, lines=tex_lines)

    # compile to pdf
    if not args.no_pdf:
        compile_success, compile_message = compile_tex_to_pdf(
            path=tex_path,
            save_tex=args.save_tex,
            show_tex_output=args.show_tex_output,
        )

        # display compile success
        if compile_success:
            msg.message(compile_message)
        else:
            msg.error(compile_message)
            return False

    msg.message('Done')

    return True
