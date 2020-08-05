from pathlib import Path
from typing import List as L

from texlite.components.common import BACKSLASH


class Equation:
    '''Represents a full-line or multi-line mathematical equation'''

    def __init__(self, equation_lines: L[str]):

        self.equation_lines = equation_lines

    def tex(self) -> str:
        '''Returns generated TeX from component'''

        # form equation section
        lines = [
            f'{BACKSLASH}begin{{align*}}',
            *[f'{line} {BACKSLASH*2}' for line in self.equation_lines],
            f'{BACKSLASH}end{{align*}}'
        ]

        return '\n'.join(lines)
