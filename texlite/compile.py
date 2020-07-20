import os
from pathlib import Path


AUXILLARY_FILE_EXTENSIONS = ['aux', 'log']


def compile_tex_to_pdf(path, save_tex=False, show_tex_output=False):

    # get base file path (tex file path without extension)
    file_path = Path(os.path.splitext(path)[0])
    file_stem = file_path.stem

    # compile to pdf using pdfLaTeX
    os.system(_get_compilation_command(file_path, show_tex_output=show_tex_output))

    # move pdf to destination
    os.system(f'mv {file_stem}.pdf {file_path}.pdf')

    # clean up auxillery files
    for extension in AUXILLARY_FILE_EXTENSIONS:
        os.system(f'rm {file_stem}.{extension}')

    # remove tex if not keeping
    if not save_tex:
        os.system(f'rm {file_path}.tex')


def _get_compilation_command(file_path, show_tex_output=False):

    # put together pdflatex command
    compilation_command = f'pdflatex {file_path}.tex'
    if show_tex_output:
        return compilation_command
    return f'{compilation_command} > {os.devnull}'
