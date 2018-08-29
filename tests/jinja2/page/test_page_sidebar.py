from pathlib import Path

import pytest
from bulmaio_jinja2.page.sidebar.models import Sidebar
from bulmaio_jinja2.utils import load_yaml

sample = Path(__file__).parents[3] / 'bulmaio_jinja2' / 'sample'


@pytest.fixture
def context_sidebar():
    pages = load_yaml('pages', base_dir=sample)
    page = pages[7]
    page_sidebar = Sidebar(**page['sidebar'])
    return dict(page_sidebar=page_sidebar)


@pytest.mark.parametrize(
    'page',
    [['test_page_sidebar.html', context_sidebar], ],
    indirect=True
)
def test_sidebar(page):
    references = page.find_all('div', class_='bio-page-sidebar')
    assert 1 == len(references)
