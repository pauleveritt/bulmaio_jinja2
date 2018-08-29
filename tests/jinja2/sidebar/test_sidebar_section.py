from pathlib import Path

import pytest
from bulmaio_jinja2.sidebar.section.models import SectionSidebar
from bulmaio_jinja2.utils import load_yaml

sample = Path(__file__).parents[3] / 'bulmaio_jinja2' / 'sample'


@pytest.fixture
def context_no_sidebar_section():
    sidebar_section = SectionSidebar()
    return dict(sidebar=sidebar_section)


@pytest.fixture
def context_sidebar_section():
    section_sidebar = load_yaml('section_sidebar', base_dir=sample)
    entries = section_sidebar['entries']
    sidebar_section = SectionSidebar(entries=entries)
    return dict(sidebar=sidebar_section)


@pytest.mark.parametrize(
    'page',
    [['test_sidebar_section.html', context_no_sidebar_section], ],
    indirect=True
)
def test_no_sidebar_section(page):
    sidebar = page.find_all('aside', class_='bd-side')
    assert 0 == len(sidebar)


@pytest.mark.parametrize(
    'page',
    [['test_sidebar_section.html', context_sidebar_section], ],
    indirect=True
)
def test_sidebar_section(page):
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
