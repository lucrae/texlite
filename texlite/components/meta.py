from texlite.components.common import BACKSLASH, BANNER_LINE, FONT_SIZES
from texlite.messages import warning


class Meta:

    def __init__(self, title=None, author=None, date=None,
                 fontsize='10pt', margin='1.6in', pagenumbers=True,
                 graphics_path=None):

        # document details
        self.title = title
        self.author = author
        self.date = date

        # document setup
        self.fontsize = fontsize # (default: 10pt)
        self.margin = margin # (default: 1.6in)

        # graphics setup
        self.graphics_path = graphics_path

    def tex(self):

        # check options
        self._check_options()

        # add meta preface
        lines = [
            r'% meta',
            f'{BACKSLASH}documentclass[{self.fontsize}]{{extarticle}}',
        ]

        # add packages
        lines += [
            r'',
            r'% packages',
            *self._packages(),
        ]

        # add optional title details
        lines += [
            r'',
            r'% document details',
            *self._document_details()
        ]

        # return joined string
        return '\n'.join(lines)

    def _check_options(self):

        # check warnings
        if self.fontsize not in FONT_SIZES:
            # extarticle font sizes can only be 8, 9, 10, 11, 12, 14, 17, 20

            self.fontsize = '10pt' # reset to default
            warning(
                'article fontsize must be one of [8pt, 9pt, 10pt, 11pt, 12pt, '
                '14pt, 17pt, 20pt], defaulting to 10pt'
            )

    def _packages(self):

        lines = []

        # include encoding specification
        lines.append(f'{BACKSLASH}usepackage[utf8]{{inputenc}}')

        # include margins
        lines.append(f'{BACKSLASH}usepackage[margin={self.margin}]'
                     f'{{geometry}}')

        # include hyperlinks
        lines.append(f'{BACKSLASH}usepackage{{hyperref}}')

        # include graphs
        if self.graphics_path:
            lines.append(f'{BACKSLASH}usepackage{{graphicx}}')
            lines.append(f'{BACKSLASH}graphicspath'
                         f'{{{{{self.graphics_path}/}}}}')

        return lines

    def _document_details(self):

        lines = []

        # add title if applicable
        if self.title:
            lines.append(f'{BACKSLASH}title{{{BACKSLASH}'
                         f'textbf{{{self.title}}}}}')

        # add author if applicable
        if self.author:
            lines.append(f'{BACKSLASH}author{{{self.author}}}')

        # add date, defaulting an empty (unshown) date
        if self.date:
            lines.append(f'{BACKSLASH}date{{{self.date}}}'),
        else:
            lines.append(f'{BACKSLASH}date{{}}')

        return lines


class DocumentBegin:

    def tex(self):
        return '\n'.join([
            BANNER_LINE,
            r'\begin{document}',
            BANNER_LINE,
        ])


class DocumentEnd:

    def tex(self):
        return '\n'.join([
            BANNER_LINE,
            r'\end{document}',
            BANNER_LINE,
        ])


class MakeTitle:

    def tex(self):
        return r'\maketitle{}'
