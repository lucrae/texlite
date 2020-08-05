import re
import os


from texlite.utils import get_os_name


class ANSI:
    '''ANSI colour interrupt codes'''

    # default/reset code
    DEFAULT = '\033[0m'

    # colour codes
    OK = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'

    # effects
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # GREEN = '\033[92m'
    # YELLOW = '\033[93m'
    # RED = '\033[91m'
    # MAGENTA = '\033[95m',
    # BLUE ='\033[94m',

    @classmethod
    def disable(self):
        self.DEFAULT = ''
        self.OK = ''
        self.WARNING = ''
        self.ERROR = ''
        self.BOLD = ''
        self.UNDERLINE = ''


# disable terminal styling if not on Linux
if get_os_name() != 'linux':
    ANSI.disable()


def _print(message: str, preface: str=None, col=ANSI.DEFAULT) -> None:

    # print text
    if preface:
        print(f'{col}{ANSI.BOLD}{preface}:{ANSI.DEFAULT} {message}')
    else:
        print(f'{col}{message}{ANSI.DEFAULT}')


def message(message: str) -> None:
    '''Prints a standard message'''

    # print message
    _print(message, preface='TeXLite', col=ANSI.OK)


def warning(message: str) -> None:
    '''Prints a warning message'''

    # print warning message
    _print(message, preface='Warning', col=ANSI.WARNING)


def error(message: str, halt: bool=False) -> None:
    '''Prints an error message'''

    # print error message
    _print(message, preface='Error', col=ANSI.ERROR)

    if halt:
        # halt program
        exit()
