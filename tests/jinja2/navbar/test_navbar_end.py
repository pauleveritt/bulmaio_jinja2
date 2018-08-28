import pytest
from bulmaio_jinja2.navbar.end.models import NavbarEnd


@pytest.fixture
def context_end():
    navbar_end = NavbarEnd(
        links=[
            dict(
                color='333',
                href='https://github.com/jgthms/bulma',
                icon='github-alt',
            )
        ]
    )

    return dict(navbar_end=navbar_end)


@pytest.mark.parametrize(
    'page',
    [['test_navbar_end.html', context_end], ],
    indirect=True
)
def test_navbar_end(page):
    a = page.find_all('a', class_='navbar-item')
    assert 1 == len(a)
    assert 'https://github.com/jgthms/bulma' == a[0].attrs['href']
    icon = a[0].find('i')
    assert 'fa-github-alt' in icon.attrs['class']
