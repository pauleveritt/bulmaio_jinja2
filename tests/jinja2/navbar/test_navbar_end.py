from pathlib import Path

import pytest
from bulmaio_jinja2.navbar.end.models import NavbarEnd
from bulmaio_jinja2.utils import load_yaml

sample = Path(__file__).parents[3] / 'bulmaio_jinja2' / 'sample'


@pytest.fixture
def context_end():
    yaml = load_yaml('navbar', base_dir=sample)
    navbar_end = NavbarEnd(**yaml['end'])

    return dict(navbar_end=navbar_end)


@pytest.mark.parametrize(
    'page',
    [['test_navbar_end.html', context_end], ],
    indirect=True
)
def test_navbar_end(page):
    a = page.find_all('a', class_='navbar-item')
    assert 2 == len(a)
    assert 'https://github.com/jgthms/bulma' == a[0].attrs['href']
    icon = a[0].find('i')
    assert 'fa-github-alt' in icon.attrs['class']
