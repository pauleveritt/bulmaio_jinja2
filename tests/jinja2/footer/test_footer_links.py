import os
from pathlib import Path

import pytest
from yaml import Loader, load

from bulmaio_jinja2.footer.links.models import FooterLinks

cwd = Path(__file__).parents[0]


def load_yaml(filename):
    fn = os.path.join(cwd, filename + '.yaml')
    with open(fn, 'r') as f:
        data = load(f, Loader=Loader)
        return data


@pytest.fixture
def context_links():
    footer_links = FooterLinks(**load_yaml('footer_links'))

    return dict(footer_links=footer_links)


@pytest.mark.parametrize(
    'page',
    [['test_footer_links.html', context_links], ],
    indirect=True
)
def test_links(page):
    link_titles = page.find('p', class_='bd-footer-link-title')
    assert 3 == len(link_titles)
