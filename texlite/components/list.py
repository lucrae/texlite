from texlite.components.common import BACKSLASH
from texlite.components.text import Text


class UnorderedList:

    def __init__(self, items):
        self.items = items

    def tex(self):

        lines = [f'{BACKSLASH}begin{{itemize}}']

        # add items
        for item in self.items:
            lines.append(f'\t{BACKSLASH}item {Text(item).tex()}')

        lines.append(f'{BACKSLASH}end{{itemize}}')

        return '\n'.join(lines)


class OrderedList:

    def __init__(self, items):
        self.items = items

    def tex(self):

        lines = [f'{BACKSLASH}begin{{enumerate}}']

        # add items
        for item in self.items:
            lines.append(f'\t{BACKSLASH}item {Text(item).tex()}')

        lines.append(f'{BACKSLASH}end{{enumerate}}')

        return '\n'.join(lines)
