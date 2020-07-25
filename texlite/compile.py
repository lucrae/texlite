import os
import subprocess
from pathlib import Path


AUXILLARY_FILE_EXTENSIONS = ['aux', 'log', 'out']


def compile_tex_to_pdf(path, save_tex=False, show_tex_output=False):

    # get base file path (tex file path without extension)
    base_path = Path(path).parents[0] / Path(path).stem
    file_stem = base_path.stem

    exit_code = call_pdflatex(base_path, show_tex_output=show_tex_output)

    # XXX: pdflatex_error code will not be handled on Windows, working fix:
    # # compile to pdf using pdfLaTeX
    # try:
    #     pdflatex_error = _call(_get_compilation_command(base_path,
    #                            show_tex_output=show_tex_output))
    # except:

    #     # NOTE: if the call completely fails, it is likely due to TeX not
    #     # being installed. On Ubuntu/Linux this will give an error code 127
    #     # but on Windows it might just completely fail.
    #     return False, ('TeX compiler could not be found. If not installed, '
    #                    'please install a TeX distribution (TeX Live '
    #                    'recommended).')

    # handle pdflatex errors
    if exit_code == 1:

        _tex_clean_up(file_stem, base_path, AUXILLARY_FILE_EXTENSIONS,
                      save_tex=False)

        return False, ('TeX could not be compiled, likely due to the '
                       'inclusion of a special character or undefined '
                       'command. Use --show-tex-output for details.')

    elif exit_code == 127:

        return False, ('TeX compiler could not be found. If not installed, '
                       'please install a TeX distribution (TeX Live '
                       'recommended).')

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


def call_pdflatex(base_path, show_tex_output=False):

    # set flags
    flags = '-halt-on-error'

    # set output pipe
    out = f'> {os.devnull}'
    if show_tex_output:
        out = '' # stdout

    # run pdflatex
    cmd = ['pdflatex', flags, base_path, out] 
    exit_code = subprocess.call(cmd)

    return exit_code


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
   