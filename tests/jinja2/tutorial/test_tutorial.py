from pathlib import Path

import pytest
from bulmaio_jinja2.footer.models import Footer
from bulmaio_jinja2.navbar.models import Navbar
from bulmaio_jinja2.site.models import Site
from bulmaio_jinja2.tutorial.models import Tutorial, TutorialSidebar
from bulmaio_jinja2.utils import load_yaml

sample = Path(__file__).parents[3] / 'bulmaio_jinja2' / 'sample'


@pytest.fixture
def context_tutorial():
    site_yaml = load_yaml('site', base_dir=sample)
    site = Site(**site_yaml)
    navbar_yaml = load_yaml('navbar', base_dir=sample)
    navbar = Navbar(**navbar_yaml)
    footer_yaml = load_yaml('footer', base_dir=sample)
    footer = Footer(**footer_yaml)
    pages = load_yaml('pages', base_dir=sample)
    tutorial = Tutorial(**pages[6])
    sidebar_yaml = load_yaml('tutorial_sidebar', base_dir=sample)
    sidebar = TutorialSidebar(**sidebar_yaml)
    return dict(site=site, navbar=navbar, page=tutorial, sidebar=sidebar,
                footer=footer)


@pytest.mark.parametrize(
    'page',
    [['test_tutorial.html', context_tutorial], ],
    indirect=True
)
def test_tutorial(page):
    body = page.find_all('main', class_='bd-main')
    assert 1 == len(body)

    sp = page.find_all('div', class_='bio-tutorial-steps-sidebar')
    assert 1 == len(sp)
