from pathlib import Path
from typing import Optional, List as L

from texlite.components.common import (
    is_number, BACKSLASH, BANNER_LINE, FONT_SIZES
)
from texlite import messages as msg
from texlite.utils import read_file_as_list


DEFAULT_PACKAGES = [
    'hyperref',
    'amsmath',
    'amssymb',
]


class Meta:
    '''Handles the meta options and setup of the document'''

    def __init__(self, title: Optional[str]=None,
                 author: Optional[str]=None,
                 date: Optional[str]=None,
                 abstract: Optional[str]=None,
                 fontsize: str='10pt',
                 margin: str='1.6in',
                 linespread: int=1.0,
                 usepackages: Optional[str]=None,
                 package_config_path: Optional[Path]=None,
                 graphics_path: Optional[Path]=None):

        # set default packages
        self.packages = DEFAULT_PACKAGES

        # set default packages
        if package_config_path:

            # use custom list
            self.packages += read_file_as_list(package_config_path)

        # declare specifiable meta options
        # NOTE: validation of options handled in `Meta._validate_options`
        # by default, defaults are None
        self.options = [
            'title',
            'author',
            'date',
            'abstract',
            'fontsize', # default: 10pt
            'margin', # default: 1.6in
            'linespread', # default: 1.0
            'usepackages',
        ]

        # document detail options
        self.title = title
        self.author = author
        self.date = date
        self.abstract = abstract

        # document setup options
        self.fontsize = fontsize
        self.margin = margin
        self.linespread = linespread

        # other
        self.usepackages = usepackages

        # graphics setup
        self.graphics_path = graphics_path

    def tex(self) -> str:
        '''Returns generated TeX from component'''

        # validate options
        self._validate_options()

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

        # add preamble commands
        lines += [
            r'',
            r'% preamble commands',
            *self._preamble_commands(),
        ]

        # add optional title details
        lines += [
            r'',
            r'% document details',
            *self._document_details()
        ]

        # return joined string
        return '\n'.join(lines)

    def _validate_options(self) -> None:
        '''Validates options to provide warnings and reset to defaults'''

        # check fontsize
        if self.fontsize not in FONT_SIZES:

            # show warning and enact default
            msg.warning(
                'Option \'fontsize\' must be one of [8pt, 9pt, 10pt, 11pt, '
                '12pt, 14pt, 17pt, 20pt]. Defaulting to 10pt.'
            )
            self.fontsize = '10pt' # reset to default

        # # check margin
        if (not is_number(self.margin[:-2]) or
                not self.margin[-2:] in ['mm', 'cm', 'pt', 'in']):

            # show warning and enact default
            msg.warning(
                'Option \'margin\' must be a number followed by one of [mm, '
                'cm, pt, in] (e.g. 0.8in). Defaulting to 1.6in.'
            )
            self.margin = '1.6in'

        # check linespread
        if not is_number(self.linespread):

            # show warning and enact default
            msg.warning(
                'Option \'linespread\' must be a float (e.g. 1.6). '
                'Defaulting to 1.0.'
            )
            self.linespread = 1.0

    def _packages(self) -> L[str]:
        '''Returns list of TeX import commands for packages'''

        lines = []

        # include encoding specification
        lines.append(f'{BACKSLASH}usepackage[utf8]{{inputenc}}')

        # include margins
        lines.append(f'{BACKSLASH}usepackage[margin={self.margin}]'
                     f'{{geometry}}')

        # include default packages
        for package in self.packages:
            lines.append(f'{BACKSLASH}usepackage{{{package}}}')

        # include extra packages
        if self.usepackages:
            extra_packages = self.usepackages.replace(' ', '').split(',')
            for package in extra_packages:
                lines.append(f'{BACKSLASH}usepackage{{{package}}} % custom')

        return lines

    def _preamble_commands(self) -> L[str]:
        '''Returns list of TeX comamands for the document preamble'''

        lines = []

        # set line spacing
        lines.append(f'{BACKSLASH}linespread{{{self.linespread}}}')

        # include path for graphics
        if self.graphics_path:

            # ensure path is POSIX
            self.graphics_path = Path(self.graphics_path).as_posix()

            lines.append(f'{BACKSLASH}usepackage{{graphicx}}')
            lines.append(f'{BACKSLASH}graphicspath'
                         f'{{{{{self.graphics_path}/}}}}')

        return lines

    def _document_details(self) -> L[str]:
        '''Returns list of TeX document detail specification commands'''

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
    '''Opens the main document section'''

    def tex(self) -> str:
        '''Returns generated TeX from component'''

        return '\n'.join([
            BANNER_LINE,
            r'\begin{document}',
            BANNER_LINE,
        ])


class DocumentEnd:
    '''Closes the main document section'''

    def tex(self) -> str:
        '''Returns generated TeX from component'''

        return '\n'.join([
            BANNER_LINE,
            r'\end{document}',
            BANNER_LINE,
        ])


class MakeTitle:
    '''Creates the title from the meta document details'''

    def __init__(self, meta: Meta):
        self.title = meta.title
        self.author = meta.author
        self.date = meta.date
        self.abstract = meta.abstract

    def tex(self) -> str:
        '''Returns generated TeX from component'''

        lines = []

        if self.title:
            lines.append(f'{BACKSLASH}maketitle{{}}')

        if self.abstract:
            lines += [
                f'{BACKSLASH}begin{{abstract}}',
                f'{self.abstract}',
                f'{BACKSLASH}end{{abstract}}'
            ]

        return '\n'.join(lines)
