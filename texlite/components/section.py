from texlite.components.common import BACKSLASH


class Section:

    def __init__(self, content, section_type='section'):
        self.section_type = section_type
        self.content = content

    def tex(self):
        return f'{BACKSLASH}{self.section_type}{{{self.content}}}'
