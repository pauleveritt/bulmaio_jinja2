from pathlib import Path

import pytest
from bulmaio_jinja2.sidebar.page.models import SidebarPublished
from bulmaio_jinja2.utils import load_yaml

sample = Path(__file__).parents[3] / 'bulmaio_jinja2' / 'sample'


@pytest.fixture
def context_no_sidebar_published():
    sidebar_published = SidebarPublished()
    return dict(sidebar_published=sidebar_published)


@pytest.fixture
def context_sidebar_published():
    sidebar_yaml = load_yaml('page_sidebar', base_dir=sample)
    published = sidebar_yaml['published']
    sidebar_published = SidebarPublished(**published)
    return dict(sidebar_published=sidebar_published)


@pytest.fixture
def context_sidebar_draft():
    sidebar_yaml = load_yaml('page_sidebar', base_dir=sample)
    published = sidebar_yaml['published']
    del published['published_date']
    sidebar_published = SidebarPublished(**published)
    return dict(sidebar_published=sidebar_published)


@pytest.mark.parametrize(
    'page',
    [['test_sidebar_page_published.html', context_no_sidebar_published], ],
    indirect=True
)
def test_no_sidebar_published(page):
    published = page.find_all('p', class_='bio-page-sidebar-published')
    assert 0 == len(published)


@pytest.mark.parametrize(
    'page',
    [['test_sidebar_page_published.html', context_sidebar_published], ],
    indirect=True
)
def test_sidebar_published(page):
    published = page.find_all('p', class_='bio-page-sidebar-published')
    assert 1 == len(published)

    published_date = page.find('span',
                               class_='bio-page-sidebar-published-date')
    e1 = 'Published\n                        on 2018-02-25'
    assert e1 == published_date.string.strip()
    published_time = page.find('span',
                               class_='bio-page-sidebar-published-time')
    e2 = '12:00'
    assert e2 == published_time.string.strip()


@pytest.mark.parametrize(
    'page',
    [['test_sidebar_page_published.html', context_sidebar_draft], ],
    indirect=True
)
def test_sidebar_draft(page):
    draft = page.find('p', class_='menu-label')
    assert 'Draft' == draft.string.strip()
