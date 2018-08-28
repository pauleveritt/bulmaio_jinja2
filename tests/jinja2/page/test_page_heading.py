from pathlib import Path

import pytest
from bulmaio_jinja2.page.heading.models import PageHeading
from bulmaio_jinja2.utils import load_yaml

sample = Path(__file__).parents[3] / 'bulmaio_jinja2' / 'sample'


@pytest.fixture
def context_heading():
    pages = load_yaml('pages', base_dir=sample)
    page3 = pages[3]
    heading = page3['heading']
    page_heading = PageHeading(**heading)
    return dict(page_heading=page_heading)


@pytest.mark.parametrize(
    'page',
    [['test_page_heading.html', context_heading], ],
    indirect=True
)
def test_heading(page):
    header = page.find('div', class_='bd-header-titles')
    title = header.find('h1', class_='title')
    assert 'Getting started with Bulma' == title.string.strip()
    subtitle = header.find('strong')
    assert '1 CSS file' == subtitle.string.strip()
