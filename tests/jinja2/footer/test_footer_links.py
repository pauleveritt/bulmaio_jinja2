from pathlib import Path

import pytest
from bulmaio_jinja2.footer.links.models import FooterLinks
from bulmaio_jinja2.utils import load_yaml

cwd = Path(__file__).parents[0]


@pytest.fixture
def context_links():
    footer_links = FooterLinks(**load_yaml('footer_links', base_dir=cwd))

    return dict(footer_links=footer_links)


@pytest.mark.parametrize(
    'page',
    [['test_footer_links.html', context_links], ],
    indirect=True
)
def test_links(page):
    link_titles = page.find('p', class_='bd-footer-link-title')
    assert 3 == len(link_titles)
