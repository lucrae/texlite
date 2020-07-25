import os
import subprocess
from pathlib import Path


AUXILLARY_FILE_EXTENSIONS = ['aux', 'log', 'out']


def compile_tex_to_pdf(path, save_tex=False, show_tex_output=False):

    # get base file path (tex file path without extension)
    base_path = Path(path).parents[0] / Path(path).stem
    file_stem = base_path.stem

    try:
        exit_code = _call_pdflatex(base_path, show_tex_output=show_tex_output)
    except FileNotFoundError:
        return False, ('TeX compiler could not be found. If not installed, '
                       'please install a TeX distribution (TeX Live '
                       'recommended).')

    # handle pdflatex errors
    if exit_code == 1:

        _tex_clean_up(file_stem, base_path, AUXILLARY_FILE_EXTENSIONS,
                      save_tex=False)

        return False, ('TeX could not be compiled, likely due to the '
                       'inclusion of a special character or undefined '
                       'command. Use --show-tex-output for details.')

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

    return True, f'Compiled document as "{base_path}.pdf"'


def _call_pdflatex(base_path, show_tex_output=False):

    # set command executable
    cmd_exe = _get_pdflatex_exe()

    # if executable not found, raise FileNotFoundError
    if not cmd_exe:
        raise FileNotFoundError

    # set flags
    cmd_args = ['-halt-on-error', base_path]

    # set keyword arguments for subprocess call
    call_kwargs = {}
    if not show_tex_output:
        call_kwargs = {
            'stdout': subprocess.PIPE,
            'stderr': subprocess.PIPE,
        }

    # run pdflatex
    cmd = [cmd_exe, *cmd_args]
    exit_code = subprocess.call(cmd, **call_kwargs)

    return exit_code


def _get_pdflatex_exe():

    # set keyword arguments for subprocess call
    call_kwargs = {
        'stdout': subprocess.PIPE,
        'stderr': subprocess.PIPE,
    }

    # attempts (in order)
    exes = [
        'pdflatex',
        '/usr/bin/pdflatex', # Ubuntu/Debian
        '/Library/TeX/texbin/pdflatex', # MacOS
    ]

    for exe in exes:
        # attempt to call which on executable
        if subprocess.call(['which', exe], **call_kwargs) == 0:
            return exe

    # return None if no attempts succeeded
    return None


def _tex_clean_up(file_stem, base_path, auxillary_file_extensions,
                  save_tex=False):

    # clean up auxillary files
    for extension in AUXILLARY_FILE_EXTENSIONS:
        if Path(f'{file_stem}.{extension}').exists():
            Path(f'{file_stem}.{extension}').unlink()

    # remove tex if not keeping
    if not save_tex:
        if Path(f'{base_path}.tex').exists():
            Path(f'{base_path}.tex').unlink()
