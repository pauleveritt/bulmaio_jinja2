from pathlib import Path

import pytest
from bulmaio_jinja2.sidebar.page.models import SidebarReferences

from bulmaio_jinja2.utils import load_yaml

sample = Path(__file__).parents[3] / 'bulmaio_jinja2' / 'sample'


@pytest.fixture
def context_no_sidebar_references():
    sidebar_references = SidebarReferences()
    return dict(sidebar_references=sidebar_references)


@pytest.fixture
def context_sidebar_references():
    sidebar_yaml = load_yaml('page_sidebar', base_dir=sample)
    published = sidebar_yaml['published']
    references = sidebar_yaml['references']
    sidebar_references = SidebarReferences(**references)
    return dict(sidebar_references=sidebar_references)


@pytest.mark.parametrize(
    'page',
    [['test_sidebar_page_references.html', context_no_sidebar_references], ],
    indirect=True
)
def test_no_sidebar_references(page):
    references = page.find_all('p', class_='bio-page-sidebar-references-group')
    assert 0 == len(references)


@pytest.mark.parametrize(
    'page',
    [['test_sidebar_page_references.html', context_sidebar_references], ],
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
