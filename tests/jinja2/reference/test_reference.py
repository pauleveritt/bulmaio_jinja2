from pathlib import Path

import pytest
from bulmaio_jinja2.footer.models import Footer
from bulmaio_jinja2.navbar.models import Navbar
from bulmaio_jinja2.reference.models import Reference
from bulmaio_jinja2.site.models import Site
from bulmaio_jinja2.tutorial.models import TutorialSidebar
from bulmaio_jinja2.utils import load_yaml

sample = Path(__file__).parents[3] / 'bulmaio_jinja2' / 'sample'


@pytest.fixture
def context_reference():
    site_yaml = load_yaml('site', base_dir=sample)
    site = Site(**site_yaml)
    navbar_yaml = load_yaml('navbar', base_dir=sample)
    navbar = Navbar(**navbar_yaml)
    footer_yaml = load_yaml('footer', base_dir=sample)
    footer = Footer(**footer_yaml)
    pages = load_yaml('pages', base_dir=sample)
    page = pages[4]
    reference = Reference(**page)
    sidebar_yaml = load_yaml('tutorial_sidebar', base_dir=sample)
    sidebar = TutorialSidebar(**sidebar_yaml)
    return dict(site=site, navbar=navbar, page=reference, sidebar=sidebar,
                footer=footer)


@pytest.mark.parametrize(
    'page',
    [['test_reference.html', context_reference], ],
    indirect=True
)
def test_reference(page):
    body = page.find_all('main', class_='bd-main')
    assert 1 == len(body)

    sl = page.find('div', class_='bio-reference-listing')

    # Logo
    logo = sl.find('img', class_='bio-common-resourcecard-logo')
    assert logo.attrs['src'].startswith('http://konpa.github.io/')
