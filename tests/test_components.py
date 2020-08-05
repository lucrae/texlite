import pytest

import argparse
from pathlib import Path

from texlite.cli import run


SHOW_TEX_OUTPUT = True

COMPONENTS_TO_TEST = [
    'meta',
    'meta_incorrect',
    'section',
    'text',
    'list',
    'nested_list',
    'figure',
    'equation',
    'abstract'
]


def _read(path):

    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


@pytest.mark.parametrize('component', COMPONENTS_TO_TEST)
def test_component(component):
    '''Test a component against its corresponding expected output'''

    # set arguments
    args = {
        'source': Path(f'tests/assets/test_components/{component}.md'),
        'save_tex': True,
        'show_tex_output': SHOW_TEX_OUTPUT,
        'no_pdf': False,
        'default_packages': None,
    }

    # execute main
    run(args=argparse.Namespace(**args))

    pair = (
        _read(Path(f'tests/assets/test_components/{component}.tex')),
        _read(Path(f'tests/assets/test_components/expected/{component}.tex'))
    )

    assert pair[0] == pair[1]

    # tear down
    Path(f'tests/assets/test_components/{component}.tex').unlink()
    Path(f'tests/assets/test_components/{component}.pdf').unlink()
