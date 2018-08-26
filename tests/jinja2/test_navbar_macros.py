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


@pytest.fixture
def context_start():
    site = Site(
        navbar=dict(
            start=[
                dict(
                    css_class='documentation',
                    accent='primary',
                    icon='book',
                    label='Documentation',
                    label_narrow='Docs',
                    href='documentation.html',
                )
            ]
        )
    )

    return dict(site=site)


@pytest.fixture
def context_end():
    site = Site(
        navbar=dict(
            end=dict(
                links=[
                    dict(
                        color='333',
                        href='https://github.com/jgthms/bulma',
                        icon='github-alt',
                    )
                ]
            )
        )
    )

    return dict(site=site)


@pytest.mark.parametrize(
    'page', [['macros_brand.html', context_brand], ], indirect=True
)
def test_brand(page):
    a = page.find('a', class_='bulmaio-brand')
    assert '/index.html' == a.attrs['href']
    logo = page.find('img', class_='bulmaio-logo-image')
    assert '_static/images/bulma-logo.png' == logo.attrs['src']
    assert 'Bulma Logo' == logo.attrs['alt']


@pytest.mark.parametrize(
    'page', [['macros_start.html', context_start], ], indirect=True
)
def test_start(page):
    a = page.find_all('a', class_='navbar-item')
    assert 1 == len(a)
    assert 'documentation.html' == a[0].attrs['href']
    assert 'bd-navbar-item-documentation' in a[0].attrs['class']
    span = a[0].find('span')
    assert 'has-text-primary' in span.attrs['class']
    icon = a[0].find('i')
    assert 'fa-book' in icon.attrs['class']


@pytest.mark.parametrize(
    'page', [['macros_end.html', context_end], ], indirect=True
)
def test_end(page):
    a = page.find_all('a', class_='navbar-item')
    assert 1 == len(a)
    assert 'https://github.com/jgthms/bulma' == a[0].attrs['href']
    icon = a[0].find('i')
    assert 'fa-github-alt' in icon.attrs['class']
