import os

def using_windows():
    '''Returns if Windows is used at runtime'''

    return os.name == 'nt'