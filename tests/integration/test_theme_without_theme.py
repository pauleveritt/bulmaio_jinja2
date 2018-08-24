"""

Simulate kaybee_bulma where you have a different theme
which uses parts of bulmaio_jinja2's Sphinx:

- Detects if included as Sphinx extensions, but not the theme

- Make sure static assets are copied

- Templates are registered, to get macros

-

"""
import pytest

pytestmark = pytest.mark.sphinx('html', testroot='theme-without-theme')


@pytest.mark.parametrize('page', ['index.html', ], indirect=True)
def test_index(page):
    # Check stuff in the head
    title = page.find('title').string
    assert 'Hello Bulmaio | Theme Without Theme' == title

    h1 = page.find('h1')
    assert 'My Theme' == h1.string

    favicon = page.find_all('link', rel='shortcut icon')[0]
    assert '_static/jetbrains_favicon.ico' == favicon.attrs['href']
    stylesheet = page.find(id='bulmaio-stylesheet')
    assert '_static/bulmaio_jinja2.css' == stylesheet.attrs['href']

    # Navbar stuff: Brand
    homepage_url = page.find(class_='bulmaio-brand')
    assert '/index.html' == homepage_url.attrs['href']
    logo = page.find(class_='bulmaio-logo-image')
    assert '_static/images/bulma-logo.png' == logo.attrs['src']
    assert 'Bulma Logo' == logo.attrs['alt']


@pytest.mark.parametrize('static_asset', ['_static/bulmaio_jinja2.css', ],
                         indirect=True)
def test_css(static_asset):
    # Ensure that the bulmaio css is copied into static
    assert '@keyframes' in static_asset


@pytest.mark.parametrize('static_asset', ['_static/bulmaio_jinja2.js', ],
                         indirect=True)
def test_js(static_asset):
    # Ensure that the bulmaio js is copied into static
    assert 'parcelRequire' in static_asset
