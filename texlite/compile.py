import os
import subprocess
from pathlib import Path

from texlite.messages import message, error


AUXILLARY_FILE_EXTENSIONS = ['aux', 'log', 'out']


def compile_tex_to_pdf(path, save_tex=False, show_tex_output=False,
                       open_with=None):

    # get base file path (tex file path without extension)
    base_path = Path(path).parents[0] / Path(path).stem
    file_stem = base_path.stem

    # compile to pdf using pdfLaTeX
    pdflatex_error = _call(_get_compilation_command(base_path,
                           show_tex_output=show_tex_output))

    if pdflatex_error:
        _tex_clean_up(file_stem, base_path, AUXILLARY_FILE_EXTENSIONS,
                      save_tex=False)

        error('TeX could not be compiled, likely due to the inclusion of an '
              'undefined control sequence. Use --show-tex-output for details.')

    # move pdf to destination
    _call(f'mv {file_stem}.pdf {base_path}.pdf')

    # clean up
    _tex_clean_up(file_stem, base_path, AUXILLARY_FILE_EXTENSIONS,
                  save_tex=save_tex)

    # display success message
    message(f'Compiled document as "{base_path}.pdf"')

    # open PDF with program
    if open_with:
        message(f'Opening "{base_path}.pdf" with "{open_with}"...')
        exit_code = _call(f'{open_with} {base_path}.pdf')
        if exit_code == 127:
            error(f'Could not open "{base_path}.pdf" with "{open_with}"')


def _call(cmd):

    # perform subprocess call in shell and return exit code
    return subprocess.call(cmd, shell=True)


def _get_compilation_command(base_path, show_tex_output=False):

    # return command for compiling pdf with pdflatex
    if show_tex_output:
        return f'pdflatex -halt-on-error {base_path}.tex'
    return f'pdflatex -halt-on-error {base_path}.tex > {os.devnull}'


def _tex_clean_up(file_stem, base_path, auxillary_file_extensions,
                  save_tex=False):

    # clean up auxillary files
    for extension in AUXILLARY_FILE_EXTENSIONS:
        _call(f'rm {file_stem}.{extension}')

    # remove tex if not keeping
    if not save_tex:
        _call(f'rm {base_path}.tex')