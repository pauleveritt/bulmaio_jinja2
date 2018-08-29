from pathlib import Path

import pytest
from bulmaio_jinja2.tutorial.steps.models import StepsListing
from bulmaio_jinja2.utils import load_yaml

sample = Path(__file__).parents[3] / 'bulmaio_jinja2' / 'sample'


@pytest.fixture
def context_no_steps_listing():
    steps_listing = StepsListing()
    return dict(steps_listing=steps_listing)


@pytest.fixture
def context_steps_listing():
    pages = load_yaml('pages', base_dir=sample)
    page = pages[6]
    steps = page['steps']
    steps_listing = StepsListing(**steps)
    return dict(steps_listing=steps_listing)


@pytest.mark.parametrize(
    'page',
    [['test_tutorial_steps_listing.html', context_no_steps_listing], ],
    indirect=True
)
def test_no_steps_listing(page):
    sl = page.find_all('div', class_='bio-tutorial-steps-listing')
    assert 0 == len(sl)


@pytest.mark.parametrize(
    'page',
    [['test_tutorial_steps_listing.html', context_steps_listing], ],
    indirect=True
)
def test_steps_listing(page):
    sl = page.find('div', class_='bio-tutorial-steps-listing')

    # Logo
    logo = sl.find('img', class_='bio-common-resourcecard-logo')
    assert logo.attrs['src'].startswith('http://konpa.github.io/')
