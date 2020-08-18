import os
import subprocess
from pathlib import Path
from typing import List

from texlite import messages as msg
from texlite.utils import get_os_name


AUXILLARY_FILE_EXTENSIONS = ['aux', 'log', 'out']


def compile_tex_to_pdf(path: Path, save_tex: bool=False,
                       show_tex_output: bool=False) -> (bool, str):
    '''Compiles a PDF from a TeX (.tex) file'''

    msg.message("Compiling...")

    # get base file path (tex file path without extension)
    base_path = Path(path).parents[0] / Path(path).stem
    file_stem = base_path.stem

    # remove previous PDF file if exists
    if Path(f'{base_path}.pdf').exists():
        Path(f'{base_path}.pdf').unlink()

    # run pdflatex
    try:
        exit_code = _call_pdflatex(base_path, show_tex_output=show_tex_output)
    except FileNotFoundError:
        return False, ('TeX PDF compiler could not be found. If not '
                       'installed, please install a TeX distribution '
                       '(https://www.latex-project.org/get).')

    # handle pdflatex errors
    if exit_code == 1:

        _tex_clean_up(file_stem, base_path, AUXILLARY_FILE_EXTENSIONS,
                      save_tex=False)

        return False, ('TeX could not be compiled, possibly due to the '
                       'inclusion of a special character or undefined '
                       'command, or due to missing packages. Use '
                       '--show-tex-output for details.')

    # move pdf to destination
    Path(f'{file_stem}.pdf').rename(Path(f'{base_path}.pdf'))

    # clean up
    _tex_clean_up(file_stem, base_path, AUXILLARY_FILE_EXTENSIONS,
                  save_tex=save_tex)

    # NOTE: this feature is prone to errors and hard to test
    # # open PDF with program
    # if open_with:
    #     msg.message(f'Opening "{base_path}.pdf" with "{open_with}"...')
    #     exit_code = _call(f'{open_with} {base_path}.pdf')
    #     if exit_code == 127:
    #         msg.error(f'Could not open "{base_path}.pdf" with "{open_with}"')

    return True, f'Saving PDF \'{base_path}.pdf\'...'


def _call_pdflatex(base_path: Path, show_tex_output: bool=False) -> int:
    '''Calls pdflatex to run the PDF compilation'''

    # set command executable
    cmd_exe = _get_pdflatex_exe()

    # set flags
    cmd_args = ['-halt-on-error', str(base_path)]

    # run pdflatex
    cmd = [cmd_exe, *cmd_args]

    if show_tex_output:
        exit_code = subprocess.call(cmd)
    else:
        with open(os.devnull, 'w') as f:
            exit_code = subprocess.call(cmd, stdout=f)

    return exit_code


def _get_pdflatex_exe() -> str:
    '''Gets the name/path of pdflatex executable in shell'''

    # XXX: the `which` method used in this function does not work in Windows,
    # so just default to pdflatex. This is a little hacky and could be
    # improved.

    if get_os_name() == 'windows':
        return 'pdflatex'

    # attempts (in order)
    exes = [
        'pdflatex',
        '/usr/bin/pdflatex',
        '/usr/local/bin/pdflatex',
        '/Library/TeX/texbin/pdflatex', # macOS
    ]

    # open devnull pipe to write subprocess calls to
    with open(os.devnull, 'w') as f:

        # iterate through attempts
        for exe in exes:

            # attempt to call which on executable
            try:
                exit_code = subprocess.call(['which', exe], stdout=f)
                if exit_code == 0:
                    return exe
            except FileNotFoundError:
                msg.warning('Search for TeX PDF compiler failed.')
                raise FileNotFoundError

    # return pdflatex as a default
    return 'pdflatex'


def _tex_clean_up(file_stem: Path, base_path: Path,
                  auxillary_file_extensions: List[str],
                  save_tex: bool=False) -> None:
    '''Cleans up auxillary files generated in PDF compilation'''

    # clean up auxillary files
    for extension in AUXILLARY_FILE_EXTENSIONS:
        if Path(f'{file_stem}.{extension}').exists():
            Path(f'{file_stem}.{extension}').unlink()

    # remove tex if not keeping
    if not save_tex:
        if Path(f'{base_path}.tex').exists():
            Path(f'{base_path}.tex').unlink()
