import os


AUXILLARY_FILE_EXTENSIONS = ['aux', 'fdb_latexmk', 'fls', 'log']


def compile_to_pdf(filename, clean_up=True):
    '''Compiles a .TeX file into a PDF using latexmk'''

    # compile to pdf
    os.system(f'latexmk --pdf {filename}.tex')

    # clean up
    if clean_up:
        for extension in AUXILLARY_FILE_EXTENSIONS:
            os.system(f'rm {filename}.{extension}')

    # verify
    return os.path.isfile(f'{filename}.pdf')


if __name__ == '__main__':

    compile_to_pdf(filename='example2')