# ANSI colour interrupts
class ANSI:
    DEFAULT = '\033[0m'

    OK = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'

    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # MAGENTA = '\033[95m',
    # BLUE ='\033[94m',

    def disable(self):
        self.DEFAULT = ''
        self.OK = ''
        self.WARNING = ''
        self.ERROR = ''
        self.BOLD = ''
        self.UNDERLINE = ''


def _print(message, preface=None, col=ANSI.DEFAULT):

    # print text
    if preface:
        print(f'{col}{ANSI.BOLD}{preface}:{ANSI.DEFAULT} {message}')
    else:
        print(f'{col}{message}{ANSI.DEFAULT}')


def message(message):

    # print message
    _print(message, preface='texlite', col=ANSI.OK)


def warning(message):

    # print warning message
    _print(message, preface='warning', col=ANSI.WARNING)


def error(message):

    # print error message
    _print(message, preface='error', col=ANSI.ERROR)

    # halt program
    exit()
