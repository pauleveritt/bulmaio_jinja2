from pathlib import Path

import pytest
from bulmaio_jinja2.footer.models import Footer
from bulmaio_jinja2.models import Site
from bulmaio_jinja2.navbar.models import Navbar
from bulmaio_jinja2.page.models import Page
from bulmaio_jinja2.utils import load_yaml

sample = Path(__file__).parents[3] / 'bulmaio_jinja2' / 'sample'


@pytest.fixture
def context_page():
    site_yaml = load_yaml('site', base_dir=sample)
    site = Site(**site_yaml)
    site.footer = Footer(**load_yaml('footer', base_dir=sample))
    navbar_yaml = load_yaml('navbar', base_dir=sample)
    navbar = Navbar(**navbar_yaml)
    pages = load_yaml('pages', base_dir=sample)
    page = Page(**pages[7])
    return dict(site=site, navbar=navbar, page=page)


@pytest.mark.parametrize(
    'page',
    [['test_page.html', context_page], ],
    indirect=True
)
def test_page(page):
    tabs_wrapper = page.find('nav', class_='bd-tabs')
