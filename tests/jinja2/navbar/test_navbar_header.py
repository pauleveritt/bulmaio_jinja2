from pathlib import Path

import pytest
from bulmaio_jinja2.navbar.models import Navbar
from bulmaio_jinja2.utils import load_yaml

sample = Path(__file__).parents[3] / 'bulmaio_jinja2' / 'sample'


@pytest.fixture
def context_header():
    yaml = load_yaml('navbar', base_dir=sample)
    navbar = Navbar(**yaml)

    return dict(navbar=navbar)


@pytest.mark.parametrize(
    'page',
    [['navbar/header.html', context_header], ],
    indirect=True
)
def test_navbar_header(page):
    pass
