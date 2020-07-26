import os
from platform import system


def get_os_name():
    '''Returns if OS is linux, windows, or macos'''

    if system() == 'Linux':
        return 'linux'
    elif system() == 'Windows':
        return 'windows'
    elif system() == 'Darwin':
        return 'macos'

    # default to linux
    return 'linux'


def using_windows():
    '''Returns if Windows is used at runtime'''

    return os.name == 'nt'