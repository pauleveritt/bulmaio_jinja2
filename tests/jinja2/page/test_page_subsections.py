from pathlib import Path

import pytest
from bulmaio_jinja2.page.subsections.models import PageSubsections
from bulmaio_jinja2.utils import load_yaml

sample = Path(__file__).parents[3] / 'bulmaio_jinja2' / 'sample'


@pytest.fixture
def context_no_subsections():
    page_subsections = PageSubsections()
    return dict(page_subsections=page_subsections)


@pytest.fixture
def context_subsections():
    pages = load_yaml('pages', base_dir=sample)
    page1 = pages[1]
    entries = page1['subsections']['entries']
    page_subsections = PageSubsections(entries=entries)
    return dict(page_subsections=page_subsections)


@pytest.mark.parametrize(
    'page',
    [['test_page_subsections.html', context_no_subsections], ],
    indirect=True
)
def test_no_subsections(page):
    subsections = page.find_all('nav', class_='bd-links')
    assert 0 == len(subsections)


@pytest.mark.parametrize(
    'page',
    [['test_page_subsections.html', context_subsections], ],
    indirect=True
)
def test_subsections(page):
    subsections = page.find_all('a', class_='bd-link')
    assert 8 == len(subsections)

    ss0_a = subsections[0]
    assert '/documentation_overview.html' == ss0_a.attrs['href']
    ss0_subtitle = ss0_a.find('p', class_='bd-link-subtitle')
    ss0_em = ss0_subtitle.find('strong')
    assert 'framework' == ss0_em.string.strip()
