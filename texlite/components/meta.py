from texlite.components.common import BACKSLASH, BANNER_LINE


class Meta:

    def __init__(self, title=None, author=None, date=None,
                 fontsize='10pt', margin='1.6in', pagenumbers=True):

        # document details
        self.title = title
        self.author = author
        self.date = date

        # document setup
        self.fontsize = fontsize # (default: 10pt)
        # NOTE: extarticle fontsize options: 8, 9, 10, 11, 12, 14, 17, 20pt
        self.margin = margin # (default: 1.6in)

    def tex(self):

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

    def _packages(self):

        lines = []

        # add encoding specification
        lines.append(f'{BACKSLASH}usepackage[utf8]{{inputenc}}')

        # add margins
        lines.append(f'{BACKSLASH}usepackage[margin={self.margin}]{{geometry}}')

        # add hyperlinks
        lines.append(f'{BACKSLASH}usepackage{{hyperref}}')

        return lines

    def _document_details(self):

        lines = []

        # add title if applicable
        if self.title:
            lines.append(f'{BACKSLASH}title{{{BACKSLASH}textbf{{{self.title}}}}}')

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
