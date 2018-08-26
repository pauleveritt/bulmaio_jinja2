import pytest

from bulmaio_jinja2.models import Site, Page


@pytest.fixture
def context_brand():
    page = Page(
        docname='about'
    )
    site = Site(
        homepage_url='/index.html',
        logo=dict(
            img_file='images/bulma-logo.png',
            alt='Bulma Logo'
        ),
    )

    return dict(site=site, page=page)


@pytest.mark.parametrize(
    'page',
    [
        ['brand.html', context_brand],
    ],
    indirect=True
)
def test_rendering(page):
    a = page.find('a', class_='bulmaio-brand')
    assert '/index.html' == a.attrs['href']
    logo = page.find('img', class_='bulmaio-logo-image')
    assert '_static/images/bulma-logo.png' == logo.attrs['src']
    assert 'Bulma Logo' == logo.attrs['alt']
