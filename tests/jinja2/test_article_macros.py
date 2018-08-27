import pytest

from bulmaio_jinja2.models import Page


@pytest.fixture
def context_no_breadcrumbs():
    page = Page(
        docname='about'
    )
    return dict(page=page)

@pytest.fixture
def context_no_subtitle():
    page = Page(
        docname='about',
        title='Some Title'
    )
    return dict(page=page)


@pytest.fixture
def context_fullpage():
    page = Page(
        docname='about',
        title='Some Title',
        subtitle='Some Subtitle',
        breadcrumbs=[
            dict(
                label='Home',
                href='/'
            ),
            dict(
                label='Documentation',
                href='/documentation.html',
                is_active=True
            ),
        ]
    )
    return dict(page=page)


@pytest.mark.parametrize(
    'page',
    [['macros_breadcrumbs.html', context_no_breadcrumbs], ],
    indirect=True
)
def test_no_breadcrumbs(page):
    bcs = page.find_all('div', class_='bd-breadcrumb')
    assert 0 == len(bcs)


@pytest.mark.parametrize(
    'page',
    [['macros_breadcrumbs.html', context_fullpage], ],
    indirect=True
)
def test_breadcrumbs(page):
    bcs = page.find_all('div', class_='bd-breadcrumb')
    assert 1 == len(bcs)
    bcsli = bcs[0].find_all('li')

    # First breadcrumb
    assert [''] == bcsli[0].attrs['class']
    a0 = bcsli[0].find('a')
    assert '/' == a0.attrs['href']
    assert 'Home' == a0.string.strip()

    # Second breadcrumb
    assert ['is-active'] == bcsli[1].attrs['class']
    a1 = bcsli[1].find('a')
    assert '/documentation.html' == a1.attrs['href']
    assert 'Documentation' == a1.string.strip()



@pytest.mark.parametrize(
    'page',
    [['macros_heading.html', context_no_subtitle], ],
    indirect=True
)
def test_no_subtitle(page):
    bcs = page.find_all('div', class_='subtitle')
    assert 0 == len(bcs)


@pytest.mark.parametrize(
    'page',
    [['macros_heading.html', context_fullpage], ],
    indirect=True
)
def test_heading(page):
    header = page.find('header')
    assert ['bd-header'] == header.attrs['class']

    # Title
    title = header.find('h1', class_='title')
    assert 'Some Title' == title.string.strip()

    # Subtitle
    subtitle = header.find('h1', class_='subtitle')
    assert 'Some Subtitle' == subtitle.string.strip()
