import os
import sys


AUXILLARY_FILE_EXTENSIONS = ['aux', 'log']


def compile_tex_to_pdf(tex_file_path, clean_up=True, keep_tex=False, verbose=False):

    # get base file path (tex file path without extension)
    file_path = os.path.splitext(tex_file_path)[0]

    # compile to pdf using pdfLaTeX
    compilation_command = f'pdflatex {file_path}.tex'
    if not verbose:
        compilation_command += f'> {os.devnull}'
    os.system(compilation_command)

    # clean up
    if clean_up:
        for extension in AUXILLARY_FILE_EXTENSIONS:
            os.system(f'rm {file_path}.{extension}')

    # remove tex if not keeping
    if not keep_tex:
        os.system(f'rm {file_path}.tex')

    # return verification of pdf creation
    return os.path.isfile(f'{file_path}.pdf')