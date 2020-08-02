import sys
import argparse

from texlite.cli import run
from texlite._version import description, __version__


def main():
    '''Entry-point for command-line calling (texlite.__main__:main)'''

    # parse command-line arguments
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('source', type=str,
                        help='path to source markdown (.md) file to parse and '
                        'compile')
    parser.add_argument('-V', '--version', action='version',
                        version=f'TeXLite {__version__}',
                        help='display version and exit')
    parser.add_argument('-t', '--save-tex', action='store_true', default=False,
                        help='save TeX (.tex) file used in compilation')
    parser.add_argument('--show-tex-output', action='store_true',
                        default=False, help='show output for TeX and pdfLaTeX '
                        'processes')
    parser.add_argument('--no-pdf', action='store_true', default=False,
                        help='save TeX (.tex) and do not generate PDF')
    parser.add_argument('--use-packages', metavar='CFG', help='Read in JSON '
                        'file with list of packages to use')
    args = parser.parse_args()

    # run texlite
    run(args=args)


if __name__ == '__main__':

    # run command-line entry-point
    main()
