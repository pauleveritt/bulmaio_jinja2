import pytest

pytestmark = pytest.mark.sphinx('html', testroot='bulmaio-theme-simple')


@pytest.mark.parametrize('page', ['index.html', ], indirect=True)
def test_index(page):
    # Check stuff in the head
    title = page.find('title').string
    assert 'Hello Bulmaio | bulmaio_jinja2' == title
    favicon = page.find_all('link', rel='shortcut icon')[0]
    assert '_static/jetbrains_favicon.ico' == favicon.attrs['href']
    stylesheet = page.find(id='bulmaio-stylesheet')
    assert '_static/css/bulmaio.css' == stylesheet.attrs['href']

    # Navbar stuff: Brand
    homepage_url = page.find(class_='bulmaio-brand')
    assert '/index.html' == homepage_url.attrs['href']
    logo = page.find(class_='bulmaio-logo-image')
    assert '_static/images/bulma-logo.png' == logo.attrs['src']
    assert 'Bulma Logo' == logo.attrs['alt']

    # Navbar stuff: Start Links
    start = page.find(class_='navbar-start')
    a = start.find('a', class_='navbar-item')
    assert 'bd-navbar-item-documentation' in a.attrs['class']
    assert 'documentation.html' == a.attrs['href']
    icon = a.find('span', class_='icon')
    assert 'has-text-primary' in icon.attrs['class']
    label = a.find('span', class_='bulmaio-menu-label')
    assert 'Documentation' == label.string.strip()


    # Navbar stuff: End Links
    end = page.find(class_='navbar-end')
    a = end.find('a', class_='navbar-item')
    assert 'https://github.com/jgthms/bulma' == a.attrs['href']

    icon = a.find('span', class_='icon')
    assert 'color: #333' == icon.attrs['style']


