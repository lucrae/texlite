from texlite.components.common import BACKSLASH


class Section:
    '''Represents a depth-aware header'''

    def __init__(self, content: str, section_type: str='section'):
        self.section_type = section_type
        self.content = content

    def tex(self) -> str:
        '''Returns generated TeX from component'''

        return f'{BACKSLASH}{self.section_type}{{{self.content}}}'
