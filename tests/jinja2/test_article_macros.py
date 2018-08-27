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
def context_no_tabs():
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
        ],
        tabs=[
            dict(
                label='Tab 1',
                href='tab1.html',
                is_active=True
            ),
            dict(
                label='Tab 2',
                href='tab2.html',
            ),
            dict(
                label='Tab 3',
                href='tab3.html',
            ),
        ]
    )
    return dict(page=page)


# Breadcrumbs

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


# Subtitle

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
    header = page.find('header', class_='bd-header')
    assert ['bd-header'] == header.attrs['class']

    # Title
    title = header.find('h1', class_='title')
    assert 'Some Title' == title.string.strip()

    # Subtitle
    subtitle = header.find('p', class_='subtitle')
    assert 'Some Subtitle' == subtitle.string.strip()


# Tabs

@pytest.mark.parametrize(
    'page',
    [['macros_tabs.html', context_no_tabs], ],
    indirect=True
)
def test_no_tabs(page):
    tabs = page.find_all('nav', class_='bd-tabs')
    assert 0 == len(tabs)


@pytest.mark.parametrize(
    'page',
    [['macros_tabs.html', context_fullpage], ],
    indirect=True
)
def test_tabs(page):
    tabs_wrapper = page.find('nav', class_='bd-tabs')
    tabs = tabs_wrapper.find_all('li')
    assert 3 == len(tabs)

    # Tab 0
    tab0 = tabs[0]
    assert ['is-active'] == tab0.attrs['class']
    tab0_a = tab0.find('a')
    assert 'tab1.html' == tab0_a.attrs['href']
    assert 'Tab 1' == tab0_a.string.strip()

    # Tab 1
    tab1 = tabs[1]
    assert [''] == tab1.attrs['class']
    tab1_a = tab1.find('a')
    assert 'tab2.html' == tab1_a.attrs['href']
    assert 'Tab 2' == tab1_a.string.strip()

