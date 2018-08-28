from pathlib import Path

import pytest
from bulmaio_jinja2.footer.links.models import FooterLinks
from bulmaio_jinja2.utils import load_yaml

sample = Path(__file__).parents[3] / 'bulmaio_jinja2' / 'sample'


@pytest.fixture
def context_links():
    yaml = load_yaml('footer', base_dir=sample)
    footer_links = FooterLinks(**yaml['links'])

    return dict(footer_links=footer_links)


@pytest.mark.parametrize(
    'page',
    [['test_footer_links.html', context_links], ],
    indirect=True
)
def test_links(page):
    link_titles = page.find('p', class_='bd-footer-link-title')
    assert 3 == len(link_titles)
