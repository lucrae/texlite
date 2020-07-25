import subprocess

from texlite.compile import _get_pdflatex_exe


def test_get_pdflatex_exe():
    '''Tests that an executable for pdflatex can be found'''

    # check exit code is 0 (success)
    assert _get_pdflatex_exe()
