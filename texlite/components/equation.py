from pathlib import Path

from texlite.components.common import BACKSLASH


class Equation:

    def __init__(self, equation_lines):

        self.equation_lines = equation_lines

    def tex(self):

        lines = [
            f'{BACKSLASH}begin{{align*}}',
            *[f'{line} {BACKSLASH*2}' for line in self.equation_lines],
            f'{BACKSLASH}end{{align*}}'
        ]

        return '\n'.join(lines)
