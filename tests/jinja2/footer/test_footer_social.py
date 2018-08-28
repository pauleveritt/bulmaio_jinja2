from pathlib import Path

import pytest
from bulmaio_jinja2.footer.social.models import FooterSocial
from bulmaio_jinja2.utils import load_yaml

sample = Path(__file__).parents[3] / 'bulmaio_jinja2' / 'sample'


@pytest.fixture
def context_social():
    yaml = load_yaml('footer', base_dir=sample)
    footer_social = FooterSocial(**yaml['social'])
    return dict(footer_social=footer_social)


@pytest.mark.parametrize(
    'page',
    [['test_footer_social.html', context_social], ],
    indirect=True
)
def test_social(page):
    title = page.find('h4', class_='bio-footer-projectitle')
    strong = title.find('strong')
    assert 'Bulma' == strong.string.strip()
    author = title.find('a')
    assert 'http://jeremy' == author.attrs['href']
    assert 'Jeremy' == author.string.strip()

    # Twitter iframe
    iframe = page.find('a', 'twitter-follow-button')
    assert 'https://twitter.com/jb' == iframe.attrs['href']
    assert '@jb' == iframe.string.strip()
