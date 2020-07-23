import argparse

from texlite.main import main


if __name__ == '__main__':

    # parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=str,
                        help='path to source markdown (.md) file to parse and '
                        'compile')
    parser.add_argument('--save-tex', action='store_true', default=False,
                        help='save TeX (.tex) file used in compilation')
    parser.add_argument('--show-tex-output', action='store_true',
                        default=False, help='show output for TeX and pdfLaTeX '
                        'processes')
    parser.add_argument('--dry', action='store_true', default=False,
                        help='don\'t generate PDF')
    args = parser.parse_args()

    # run texlite
    main(args=args)
