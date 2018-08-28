from pathlib import Path

import pytest

from bulmaio_jinja2.navbar.brand.models import NavbarBrand
from bulmaio_jinja2.utils import load_yaml

sample = Path(__file__).parents[3] / 'bulmaio_jinja2' / 'sample'


@pytest.fixture
def context_brand():
    yaml = load_yaml('navbar', base_dir=sample)
    navbar_brand = NavbarBrand(**yaml['brand'])

    return dict(navbar_brand=navbar_brand)


@pytest.mark.parametrize(
    'page',
    [['test_navbar_brand.html', context_brand], ],
    indirect=True
)
def test_navbar_brand(page):
    a = page.find('a', class_='bio-navbar-brand')
    assert '/index.html' == a.attrs['href']
    logo = page.find('img', class_='bio-navbar-logo-image')
    assert 'images/bulma-logo.png' == logo.attrs['src']
    assert 'Bulma Logo' == logo.attrs['alt']

    github = page.find('a', class_='bio-navbar-brand-github')
    assert 'http://github' == github.attrs['href']
    twitter = page.find('a', class_='bio-navbar-brand-twitter')
    assert 'http://twitter' == twitter.attrs['href']
