import json
import os
from platform import system
from pathlib import Path
from typing import Union, List as L

from texlite import messages as msg


def get_os_name() -> str:
    '''Returns if OS is linux, windows, or macos'''

    if system() == 'Linux':
        return 'linux'
    elif system() == 'Windows':
        return 'windows'
    elif system() == 'Darwin':
        return 'macos'

    # default to linux
    return 'linux'


def read_json(path: Path) -> Union[dict, list]:
    '''Reads in JSON (.json) file as a dictionary or list'''

    try:
        with open(Path(path)) as f:
            return json.load(f)
    except FileNotFoundError:
        msg.error(f'JSON file \'{path}\' not found', halt=True)


def read_file_as_list(path: Path) -> L[str]:
    '''Reads a text (.txt) file and return list of file lines'''

    try:
        with open(Path(path)) as f:
            return [line.strip('\n') for line in f.readlines()]
    except FileNotFoundError:
        msg.error(f'File \'{path}\' not found', halt=True)
