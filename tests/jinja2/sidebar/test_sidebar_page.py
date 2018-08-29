from pathlib import Path

import pytest
from bulmaio_jinja2.sidebar.page.models import PageSidebar
from bulmaio_jinja2.utils import load_yaml

sample = Path(__file__).parents[3] / 'bulmaio_jinja2' / 'sample'


@pytest.fixture
def context_sidebar():
    sidebar_yaml = load_yaml('page_sidebar', base_dir=sample)
    page_sidebar = PageSidebar(**sidebar_yaml)
    return dict(page_sidebar=page_sidebar)


@pytest.mark.parametrize(
    'page',
    [['test_sidebar_page.html', context_sidebar], ],
    indirect=True
)
def test_sidebar(page):
    references = page.find_all('div', class_='bio-page-sidebar')
    assert 1 == len(references)
