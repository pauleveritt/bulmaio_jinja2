from pathlib import Path

import pytest
from bulmaio_jinja2.reference.models import Reference
from bulmaio_jinja2.utils import load_yaml

sample = Path(__file__).parents[3] / 'bulmaio_jinja2' / 'sample'


@pytest.fixture
def context_no_references():
    pages = load_yaml('pages', base_dir=sample)
    page = pages[4]
    page['entries'] = []
    reference = Reference(**page)
    return dict(reference=reference)


@pytest.fixture
def context_references():
    pages = load_yaml('pages', base_dir=sample)
    page = pages[4]
    reference = Reference(**page)
    return dict(reference=reference)


@pytest.mark.parametrize(
    'page',
    [['test_reference_listing.html', context_no_references], ],
    indirect=True
)
def test_no_reference_listing(page):
    sl = page.find_all('div', class_='bio-reference-listing')
    assert 0 == len(sl)


@pytest.mark.parametrize(
    'page',
    [['test_reference_listing.html', context_references], ],
    indirect=True
)
def test_reference_listing(page):
    sl = page.find('div', class_='bio-reference-listing')

    # Logo
    logo = sl.find('img', class_='bio-common-resourcecard-logo')
    assert logo.attrs['src'].startswith('http://konpa.github.io/')
