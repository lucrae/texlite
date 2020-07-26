import re
from pathlib import Path
from setuptools import setup, find_packages

from texlite._version import description, __version__

# read in README file for long description
with open(Path('docs/DESCRIPTION.md'), 'r') as f:

    long_description = f.read()

    # # set up html regex pattern to filter README
    # html_re = re.compile(r'<.*>')
    # long_description_lines = []

    # # read in README lines and append non-HTML non-empty lines
    # for line in f.readlines():
    #     if not re.search(html_re, line) and not line == '\n':
    #         long_description_lines.append(line)

    # # form long description
    # long_description = '\n'.join(long_description_lines)


# set up package details
setup(
    name='texlite',
    version=__version__,
    author='Lucien Rae Gentil',
    author_email='lucienraegentil@gmail.com',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/lucrae/texlite',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'texlite = texlite.__main__:main'
        ]
    },
    python_requires='>=3.6',
)
