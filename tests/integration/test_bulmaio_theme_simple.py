import pytest

pytestmark = pytest.mark.sphinx('html', testroot='bulmaio-theme-simple')


@pytest.mark.parametrize('page', ['index.html', ], indirect=True)
def test_index(page):
    # Make sure the page title is what you expect
    title = page.find('h1').contents[0].strip()
    assert 'Hello Bulmaio' == title
