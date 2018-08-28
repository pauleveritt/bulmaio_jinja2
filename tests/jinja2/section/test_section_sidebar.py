from pathlib import Path

import pytest
from bulmaio_jinja2.section.sidebar.models import SectionSidebar
from bulmaio_jinja2.utils import load_yaml

sample = Path(__file__).parents[3] / 'bulmaio_jinja2' / 'sample'


@pytest.fixture
def context_no_section_sidebar():
    section_sidebar = SectionSidebar()
    return dict(section_sidebar=section_sidebar)


@pytest.fixture
def context_section_sidebar():
    site = load_yaml('site', base_dir=sample)
    entries = site['section_sidebar']['entries']
    section_sidebar = SectionSidebar(entries=entries)
    return dict(section_sidebar=section_sidebar)


@pytest.mark.parametrize(
    'page',
    [['test_section_sidebar.html', context_no_section_sidebar], ],
    indirect=True
)
def test_no_section_sidebar(page):
    sidebar = page.find_all('aside', class_='bd-side')
    assert 0 == len(sidebar)


@pytest.mark.parametrize(
    'page',
    [['test_section_sidebar.html', context_section_sidebar], ],
    indirect=True
)
def test_section_sidebar(page):
    sidebar = page.find('aside', class_='bd-side')
    categories = sidebar.find_all('div', 'bd-category')
    assert 8 == len(categories)

    # Category 0
    c0 = categories[0]
    assert ['bd-category', ''] == c0.attrs['class']
    category_list = c0.find('ul')
    c0_entries = category_list.find_all('a')
    assert 7 == len(c0_entries)
    assert '/documentation_overview_start.html' == c0_entries[0].attrs['href']

    # Category 3
    c3 = categories[3]
    c3_is_new = c3.find_all('span', class_='tag is-success')
    assert 1 == len(c3_is_new)
