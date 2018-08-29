from pathlib import Path

import pytest
from bulmaio_jinja2.footer.models import Footer
from bulmaio_jinja2.navbar.models import Navbar
from bulmaio_jinja2.section.models import Section
from bulmaio_jinja2.sidebar.section.models import SectionSidebar
from bulmaio_jinja2.site.models import Site
from bulmaio_jinja2.utils import load_yaml

sample = Path(__file__).parents[3] / 'bulmaio_jinja2' / 'sample'


@pytest.fixture
def context_section():
    site_yaml = load_yaml('site', base_dir=sample)
    site = Site(**site_yaml)
    navbar_yaml = load_yaml('navbar', base_dir=sample)
    navbar = Navbar(**navbar_yaml)
    footer_yaml = load_yaml('footer', base_dir=sample)
    footer = Footer(**footer_yaml)
    pages = load_yaml('pages', base_dir=sample)
    section = Section(**pages[1])
    section_sidebar = load_yaml('section_sidebar', base_dir=sample)
    sidebar = SectionSidebar(**section_sidebar)
    return dict(site=site, navbar=navbar, page=section, sidebar=sidebar,
                footer=footer)


@pytest.mark.parametrize(
    'page',
    [['test_section.html', context_section], ],
    indirect=True
)
def test_section(page):
    body = page.find_all('main', class_='bd-main')
    assert 1 == len(body)
