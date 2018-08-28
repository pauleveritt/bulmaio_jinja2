from pathlib import Path

import pytest
from bulmaio_jinja2.page.breadcrumbs.models import PageBreadcrumbs
from bulmaio_jinja2.utils import load_yaml

sample = Path(__file__).parents[3] / 'bulmaio_jinja2' / 'sample'


@pytest.fixture
def context_no_breadcrumbs():
    page_breadcrumbs = PageBreadcrumbs(**dict())
    return dict(page_breadcrumbs=page_breadcrumbs)


@pytest.fixture
def context_breadcrumbs():
    pages = load_yaml('pages', base_dir=sample)
    page3 = pages[3]
    breadcrumbs = page3['breadcrumbs']
    page_breadcrumbs = PageBreadcrumbs(**breadcrumbs)
    return dict(page_breadcrumbs=page_breadcrumbs)


@pytest.mark.parametrize(
    'page',
    [['test_page_breadcrumbs.html', context_no_breadcrumbs], ],
    indirect=True
)
def test_no_breadcrumbs(page):
    bcs = page.find_all('div', class_='bd-breadcrumb')
    assert 0 == len(bcs)

    # Prev/next
    prevnext = page.find_all('bd-prev-next')
    assert 0 == len(prevnext)


@pytest.mark.parametrize(
    'page',
    [['test_page_breadcrumbs.html', context_breadcrumbs], ],
    indirect=True
)
def test_breadcrumbs(page):
    bcs = page.find_all('div', class_='bd-breadcrumb')
    assert 1 == len(bcs)
    bcsli = bcs[0].find_all('li')

    # First breadcrumb
    assert [''] == bcsli[0].attrs['class']
    a0 = bcsli[0].find('a')
    assert '/' == a0.attrs['href']
    assert 'Home' == a0.string.strip()

    # Second breadcrumb
    assert [''] == bcsli[1].attrs['class']
    a1 = bcsli[1].find('a')
    assert '/documentation.html' == a1.attrs['href']
    assert 'Documentation' == a1.string.strip()

    # Third breadcrumb
    assert [''] == bcsli[2].attrs['class']
    a1 = bcsli[2].find('a')
    assert '/documentation_overview.html' == a1.attrs['href']
    assert 'Overview' == a1.string.strip()

    # Fourth breadcrumb
    assert ['is-active'] == bcsli[3].attrs['class']
    a1 = bcsli[3].find('a')
    assert '/documentation_overview_start.html' == a1.attrs['href']
    assert 'Start' == a1.string.strip()

    # Prev/next
    breadcrumbs = bcs[0]
    prevnext = breadcrumbs.find('nav', 'bd-prev-next')
    prev = prevnext.find_all('a')[0]
    assert 'Some Previous' == prev.attrs['title']
    assert '/some_previous.html' == prev.attrs['href']
    next = prevnext.find_all('a')[1]
    assert 'Some Next' == next.attrs['title']
    assert '/some_next.html' == next.attrs['href']
