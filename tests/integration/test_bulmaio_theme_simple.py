import pytest

pytestmark = pytest.mark.sphinx('html', testroot='bulmaio-theme-simple')


@pytest.mark.parametrize('page', ['index.html', ], indirect=True)
def test_index(page):
    # Check stuff in the head
    title = page.find('title').string
    assert 'Hello Bulmaio | bulmaio_jinja2' == title
    favicon = page.find_all('link', rel='shortcut icon')[0]
    assert '_static/jetbrains_favicon.ico' == favicon.attrs['href']
    stylesheet = page.find(id='bulmaio-jinja2-styleshet')
    assert '_static/css/bulmaio.css' == stylesheet.attrs['href']

    # title = page.find('h1').contents[0].strip()
    # assert 'Hello Bulmaio' == title
