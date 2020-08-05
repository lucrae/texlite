from pathlib import Path

from texlite import messages as msg
from texlite.components.common import BACKSLASH
from texlite.components.text import Text


class Figure:
    '''Represents an image, optionally with a caption'''

    def __init__(self, graphics_path: Path, image_path: Path,
                 caption_text: str='',
                 graphics_width: str=f'{BACKSLASH}textwidth'):

        # set details
        self.graphics_path = graphics_path
        self.image_path = image_path
        self.caption_text = caption_text
        self.graphics_width = graphics_width

    def tex(self) -> str:
        '''Returns generated TeX from component'''

        # check if image exists
        full_path = Path(self.graphics_path) / Path(self.image_path)
        if not Path(full_path).exists():
            msg.warning(f'Image "{full_path}" could not be found. Replacing '
                        'with placeholder text.')

            graphics = ([
                f'{BACKSLASH}texttt{{Image Not Found}}',
            ])
        else:
            graphics = [
                f'{BACKSLASH}includegraphics[width={self.graphics_width}]'
                f'{{{self.image_path}}}',
            ]

        # form figure
        if self.caption_text:
            lines = [
                f'{BACKSLASH}begin{{figure}}[h!]',
                f'{BACKSLASH}centering',
                *graphics,
                f'{BACKSLASH}caption{{{Text(self.caption_text).tex()}}}'
                f'{BACKSLASH}end{{figure}}',
            ]
        else:
            lines = [
                f'{BACKSLASH}begin{{figure}}[h!]',
                f'{BACKSLASH}centering',
                *graphics,
                f'{BACKSLASH}end{{figure}}',
            ]

        return '\n'.join(lines)
