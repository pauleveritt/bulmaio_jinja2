from pathlib import Path

import pytest
from bulmaio_jinja2.navbar.start.models import NavbarStart
from bulmaio_jinja2.utils import load_yaml

sample = Path(__file__).parents[3] / 'bulmaio_jinja2' / 'sample'


@pytest.fixture
def context_start():
    yaml = load_yaml('navbar', base_dir=sample)
    navbar_start = NavbarStart(**yaml['start'])

    return dict(navbar_start=navbar_start)


@pytest.mark.parametrize(
    'page',
    [['test_navbar_start.html', context_start], ],
    indirect=True
)
def test_navbar_start(page):
    a = page.find_all('a', class_='navbar-item')
    assert 8 == len(a)
    assert '/documentation.html' == a[0].attrs['href']
    assert 'bd-navbar-item-documentation' in a[0].attrs['class']
    span = a[0].find('span')
    assert 'has-text-primary' in span.attrs['class']
    icon = a[0].find('i')
    assert 'fa-book' in icon.attrs['class']

    # Let's look at the dropdown menu
    dropdown = page.find('div', class_='has-dropdown')
    dropdown_a = dropdown.find('a', class_='bio-dropdown-main')
    assert '/more.html' == dropdown_a.attrs['href']
    assert 'More' == dropdown_a.string.strip()
    submenu = dropdown.find('div', class_='navbar-dropdown')
    submenu_entries = submenu.find_all('a', class_='navbar-item')
    assert 3 == len(submenu_entries)
    se0 = submenu_entries[0]
    assert '/more/start.html' == se0.attrs['href']
    se0_span = se0.find('span', class_='icon')
    assert 'has-text-success' in se0_span.attrs['class']
    se0_i = se0.find('i')
    assert 'fa-rocket' in se0_i.attrs['class']
    se0_strong = se0.find('strong')
    assert 'Bulma start' == se0_strong.string.strip()
    se0_description = se0.find('span', class_='bio-dropdown-description')
    assert 'Docs' == se0_description.string.strip()
    se0_br = se0.find_all('br')
    assert 1 == len(se0_br)

    # Make sure br on second one
    se1_br = submenu_entries[1].find_all('br')
    assert 1 == len(se1_br)
