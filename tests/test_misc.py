import subprocess


def test_pdflatex():
    '''Tests if pdflatex can be used'''

    result = subprocess.call(['which', 'pdflatex'])

    # check exit code is 0 (success)
    assert result == 0
