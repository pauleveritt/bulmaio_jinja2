from pathlib import Path

import pytest
from bulmaio_jinja2.page.sidebar.models import SidebarReferences

from bulmaio_jinja2.utils import load_yaml

sample = Path(__file__).parents[3] / 'bulmaio_jinja2' / 'sample'


@pytest.fixture
def context_no_sidebar_references():
    sidebar_references = SidebarReferences()
    return dict(sidebar_references=sidebar_references)


@pytest.fixture
def context_sidebar_references():
    pages = load_yaml('pages', base_dir=sample)
    page = pages[7]
    references = page['sidebar']['references']
    sidebar_references = SidebarReferences(**references)
    return dict(sidebar_references=sidebar_references)


@pytest.mark.parametrize(
    'page',
    [['test_page_sidebar_references.html', context_no_sidebar_references], ],
    indirect=True
)
def test_no_sidebar_references(page):
    references = page.find_all('p', class_='bio-page-sidebar-references-group')
    assert 0 == len(references)


@pytest.mark.parametrize(
    'page',
    [['test_page_sidebar_references.html', context_sidebar_references], ],
    indirect=True
)
def test_sidebar_references(page):
    references = page.find_all('div',
                               class_='bio-page-sidebar-references-group')
    assert 2 == len(references)

    # First
    ref0 = references[0]
    reftype = ref0.find('span', class_='bio-page-sidebar-references-reftype')
    assert 'Technology' == reftype.string.strip()
    a = ref0.find('a', class_='bio-page-sidebar-references-href')
    assert 'http://angular' == a.attrs['href']
    label = ref0.find('span', class_='bio-page-sidebar-references-label')
    assert 'angular' == label.string.strip()
