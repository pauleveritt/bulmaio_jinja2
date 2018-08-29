from pathlib import Path

import pytest
from bulmaio_jinja2.footer.models import Footer
from bulmaio_jinja2.navbar.models import Navbar
from bulmaio_jinja2.page.models import Page
from bulmaio_jinja2.sidebar.page.models import PageSidebar
from bulmaio_jinja2.site.models import Site
from bulmaio_jinja2.utils import load_yaml

sample = Path(__file__).parents[3] / 'bulmaio_jinja2' / 'sample'


@pytest.fixture
def context_page():
    site_yaml = load_yaml('site', base_dir=sample)
    site = Site(**site_yaml)
    navbar_yaml = load_yaml('navbar', base_dir=sample)
    navbar = Navbar(**navbar_yaml)
    footer_yaml = load_yaml('footer', base_dir=sample)
    footer = Footer(**footer_yaml)
    pages = load_yaml('pages', base_dir=sample)
    page = Page(**pages[7])
    sidebar_yaml = load_yaml('page_sidebar', base_dir=sample)
    sidebar = PageSidebar(**sidebar_yaml)
    return dict(site=site, navbar=navbar, footer=footer, sidebar=sidebar,
                page=page)


@pytest.mark.parametrize(
    'page',
    [['test_page.html', context_page], ],
    indirect=True
)
def test_page(page):
    body = page.find_all('main', class_='bd-main')
    assert 1 == len(body)
