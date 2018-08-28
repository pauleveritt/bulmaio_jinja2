from pathlib import Path

import pytest
from bulmaio_jinja2.page.tabs.models import PageTabs
from bulmaio_jinja2.utils import load_yaml

sample = Path(__file__).parents[3] / 'bulmaio_jinja2' / 'sample'


@pytest.fixture
def context_no_tabs():
    page_tabs = PageTabs()
    return dict(page_tabs=page_tabs)


@pytest.fixture
def context_tabs():
    pages = load_yaml('pages', base_dir=sample)
    page3 = pages[3]
    entries = page3['tabs']['entries']
    page_tabs = PageTabs(entries=entries)
    return dict(page_tabs=page_tabs)


@pytest.mark.parametrize(
    'page',
    [['test_page_tabs.html', context_no_tabs], ],
    indirect=True
)
def test_no_tabs(page):
    tabs = page.find_all('nav', class_='bd-tabs')
    assert 0 == len(tabs)


@pytest.mark.parametrize(
    'page',
    [['test_page_tabs.html', context_tabs], ],
    indirect=True
)
def test_tabs(page):
    tabs_wrapper = page.find('nav', class_='bd-tabs')
    tabs = tabs_wrapper.find_all('li')
    assert 7 == len(tabs)

    # Tab 0
    tab0 = tabs[0]
    assert ['is-active'] == tab0.attrs['class']
    tab0_a = tab0.find('a')
    assert '/documentation_overview_start.html' == tab0_a.attrs['href']
    assert 'Start' == tab0_a.string.strip()

    # Tab 1
    tab1 = tabs[1]
    assert [''] == tab1.attrs['class']
    tab1_a = tab1.find('a')
    assert '/documentation_overview_start.html' == tab1_a.attrs['href']
    assert 'Classes' == tab1_a.string.strip()
