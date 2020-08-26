import sys
import argparse

from texlite.cli import run
from texlite._version import description, __version__


def main() -> None:
    '''Entry-point for command-line calling (texlite.__main__:main)'''

    # parse command-line arguments
    parser = argparse.ArgumentParser(
        usage='texlite [options] <source>',
        description=description,
        epilog='For more information go to https://github.com/lucrae/texlite.'
    )
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
    parser.add_argument('--default-packages', metavar='F', help='use text '
                        '(.txt) file to specify a custom set of default '
                        'packages to use (one line per package name)')
    args = parser.parse_args()

    # run texlite
    run(args=args)


if __name__ == '__main__':

    # run command-line entry-point
    main()
