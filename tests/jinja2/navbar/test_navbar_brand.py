import pytest

from bulmaio_jinja2.navbar.brand.models import NavbarBrand


@pytest.fixture
def context_brand():
    navbar_brand = NavbarBrand(
        homepage_href='../../index.html',
        img_src='images/bulma-logo.png',
        alt='Bulma Logo',
        github_url='http://github',
        twitter_url='http://twitter',
    )

    return dict(navbar_brand=navbar_brand)


@pytest.mark.parametrize(
    'page',
    [['test_navbar_brand.html', context_brand], ],
    indirect=True
)
def test_navbar_brand(page):
    a = page.find('a', class_='bio-navbar-brand')
    assert '../../index.html' == a.attrs['href']
    logo = page.find('img', class_='bio-navbar-logo-image')
    assert 'images/bulma-logo.png' == logo.attrs['src']
    assert 'Bulma Logo' == logo.attrs['alt']

    github = page.find('a', class_='bio-navbar-brand-github')
    assert 'http://github' == github.attrs['href']
    twitter = page.find('a', class_='bio-navbar-brand-twitter')
    assert 'http://twitter' == twitter.attrs['href']
