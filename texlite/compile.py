import os
import subprocess
from pathlib import Path


AUXILLARY_FILE_EXTENSIONS = ['aux', 'log', 'out']


def compile_tex_to_pdf(path, save_tex=False, show_tex_output=False,
                       dry=False):

    # get base file path (tex file path without extension)
    base_path = Path(path).parents[0] / Path(path).stem
    file_stem = base_path.stem

    # compile to pdf using pdfLaTeX
    pdflatex_error = _call(_get_compilation_command(base_path,
                           show_tex_output=show_tex_output, dry=dry))

    # handle pdflatex errors
    if pdflatex_error == 1:

        _tex_clean_up(file_stem, base_path, AUXILLARY_FILE_EXTENSIONS,
                      save_tex=False)

        return False, ('TeX could not be compiled, likely due to the '
                       'inclusion of a special character or undefined '
                       'command. Use --show-tex-output for details.')

    elif pdflatex_error == 127:

        return False, ('TeX compiler could not be found. If not installed, '
                       'please install a TeX distribution (TeX Live or MiKTeX '
                       'recommended).')

    # move pdf (if created) to destination
    if not dry:
        os.rename(f'{file_stem}.pdf', f'{base_path}.pdf')

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


def _call(cmd):

    # perform subprocess call in shell and return exit code
    # NOTE: use this only if there are no built-in os functions for the task
    return subprocess.call(cmd, shell=True)


def _tex_clean_up(file_stem, base_path, auxillary_file_extensions,
                  save_tex=False):

    # clean up auxillary files
    for extension in AUXILLARY_FILE_EXTENSIONS:
        os.remove(f'{file_stem}.{extension}')

    # remove tex if not keeping
    if not save_tex:
        os.remove(f'{base_path}.tex')


def _get_compilation_command(base_path, show_tex_output=False, dry=False):

    # set flags
    flags = '-halt-on-error'
    if dry:
        flags += ' -draftmode'

    # set output pipe
    out = f'> {os.devnull}'
    if show_tex_output:
        out = '' # stdout

    # return command for compiling pdf with pdflatex
    return f'pdflatex {flags} {base_path}.tex {out}'
