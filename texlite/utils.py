import json
import os
from platform import system
from pathlib import Path


from texlite import messages as msg


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


def read_json(path):
    '''Reads in json file as Python object'''

    try:
        with open(Path(path)) as f:
            return json.load(f)
    except FileNotFoundError:
        msg.error(f'JSON file "{path}" could not be found', halt=True)


def read_file_as_list(path):

    try:
        with open(Path(path)) as f:
            return [line.strip('\n') for line in f.readlines()]
    except FileNotFoundError:
        msg.error(f'File "{path}" could not be found', halt=True)
