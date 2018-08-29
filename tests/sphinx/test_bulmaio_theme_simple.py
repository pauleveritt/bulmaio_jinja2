import pytest

pytestmark = pytest.mark.sphinx('html', testroot='bulmaio-theme-simple')


@pytest.mark.parametrize('page', ['index.html', ], indirect=True)
def test_index(page):
    # Check stuff in the head
    title = page.find('title').string
    assert 'Hello Bulmaio | Bulma: a modern CSS framework based on Flexbox' == title
    favicon = page.find_all('link', rel='shortcut icon')[0]
    assert '_static/favicons/favicon.ico' == favicon.attrs['href']
    stylesheet = page.find(id='bulmaio-stylesheet')
    assert '_static/bulmaio_jinja2.css' == stylesheet.attrs['href']

    # Navbar stuff: Brand
    logo = page.find('img', class_='bio-navbar-logo-image')
    assert 'images/bulma-logo.png' == logo.attrs['src']
    assert 'Bulma Logo' == logo.attrs['alt']

    github = page.find('a', class_='bio-navbar-brand-github')
    assert 'http://github' == github.attrs['href']
    twitter = page.find('a', class_='bio-navbar-brand-twitter')
    assert 'http://twitter' == twitter.attrs['href']
