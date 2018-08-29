from pathlib import Path

import pytest
from bulmaio_jinja2.common.resource_card.models import ResourceCard
from bulmaio_jinja2.utils import load_yaml

sample = Path(__file__).parents[3] / 'bulmaio_jinja2' / 'sample'


@pytest.fixture
def context_resource_card():
    pages = load_yaml('pages', base_dir=sample)
    page = pages[6]
    step = page['steps']['entries'][0]
    resource_card = ResourceCard(**step)
    return dict(resource_card=resource_card)


@pytest.mark.parametrize(
    'page',
    [['test_resource_card.html', context_resource_card], ],
    indirect=True
)
def test_resource_card(page):
    rc = page.find('div', class_='bio-common-resourcecard')

    # Logo
    logo = rc.find('img', class_='bio-common-resourcecard-logo')
    assert logo.attrs['src'].startswith('http://konpa.github.io/')

    # Resource data
    props = rc.find('div', class_='bio-common-resourcecard-props')
    a = props.find('a')
    assert '/tutorial_project_setup.html' == a.attrs['href']
    strong = props.find('strong')
    assert 'Project Setup' == strong.string.strip()
    span = props.find('span')
    assert span.string.strip().startswith('Use PyCharm')

    # Author
    author = rc.find('a', class_='bio-card-author')
    assert 'http://site' == author.attrs['href']
    img = author.find('img')
    assert img.attrs['src'].startswith('https://pauleveritt')

    # References
    references = rc.find('span', class_='bio-common-card-references')
    tags = references.find_all('a')
    assert 2 == len(tags)
    assert 'http://react' == tags[0].attrs['href']

    # Duration
    duration = rc.find('span', class_='bio-common-card-duration')
    span = duration.find_all('span')
    assert '2m32s' == span[1].string.strip()

    # Published
    published = rc.find('span', class_='bio-common-card-published')
    assert '2018-02-25' == published.string.strip()