from texlite.components.common import BACKSLASH
from texlite.components.text import Text


class List:

    def __init__(self, items, ordered=False):
        self.items = items
        self.ordered = ordered

    def tex(self):

        lines = []

        # add begin
        if self.ordered:
            lines.append(f'{BACKSLASH}begin{{enumerate}}')
        else:
            lines.append(f'{BACKSLASH}begin{{itemize}}')

        # add items
        for item in self.items:

            # parse nested list
            if type(item) == type(self):
                lines.append(f'{item.tex()}')

            # parse list item
            else:
                lines.append(f'{BACKSLASH}item {Text(item).tex()}')

        # add end
        if self.ordered:
            lines.append(f'{BACKSLASH}end{{enumerate}}')
        else:
            lines.append(f'{BACKSLASH}end{{itemize}}')

        return '\n'.join(lines)
