from pathlib import Path

import pytest
from bulmaio_jinja2.sidebar.page.models import SidebarPrevNext
from bulmaio_jinja2.utils import load_yaml

sample = Path(__file__).parents[3] / 'bulmaio_jinja2' / 'sample'


@pytest.fixture
def context_no_sidebar_prevnext():
    sidebar_prev_next = SidebarPrevNext()
    return dict(sidebar_prev_next=sidebar_prev_next)


@pytest.fixture
def context_sidebar_prevnext():
    sidebar_yaml = load_yaml('page_sidebar', base_dir=sample)
    prev_next = sidebar_yaml['prev_next']
    sidebar_prev_next = SidebarPrevNext(**prev_next)
    return dict(sidebar_prev_next=sidebar_prev_next)



@pytest.mark.parametrize(
    'page',
    [['test_sidebar_page_prevnext.html', context_no_sidebar_prevnext], ],
    indirect=True
)
def test_no_sidebar_prevnext(page):
    prev = page.find_all('p', class_='bio-page-sidebar-prev-label')
    assert 0 == len(prev)
    next = page.find_all('p', class_='bio-page-sidebar-next-label')
    assert 0 == len(next)


@pytest.mark.parametrize(
    'page',
    [['test_sidebar_page_prevnext.html', context_sidebar_prevnext], ],
    indirect=True
)
def test_sidebar_prevnext(page):
    prev_list = page.find('ul', class_='bio-page-sidebar-prev-list')
    pla = prev_list.find('a')
    assert 'Previous Doc' == pla.string.strip()
    assert 'http://prev' == pla.attrs['href']
    next_list = page.find('ul', class_='bio-page-sidebar-next-list')
    nla = next_list.find('a')
    assert 'Next Doc' == nla.string.strip()
    assert 'http://next' == nla.attrs['href']
