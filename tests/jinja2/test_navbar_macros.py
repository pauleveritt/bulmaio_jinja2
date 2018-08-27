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
                ),
                dict(
                    css_class='more',
                    accent='link',
                    icon='plus',
                    label='More',
                    href='more.html',
                    submenu=[
                        dict(
                            css_class='more1',
                            accent='link',
                            icon='plus',
                            label='More1',
                            href='more1.html',
                            description='More1 Description'
                        ),
                        dict(
                            css_class='more2',
                            accent='link',
                            icon='plus',
                            label='More2',
                            href='more2.html',
                        ),
                    ]
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
    assert 3 == len(a)
    assert 'documentation.html' == a[0].attrs['href']
    assert 'bd-navbar-item-documentation' in a[0].attrs['class']
    span = a[0].find('span')
    assert 'has-text-primary' in span.attrs['class']
    icon = a[0].find('i')
    assert 'fa-book' in icon.attrs['class']

    # Let's look at the dropdown menu
    dropdown = page.find('div', class_='has-dropdown')
    dropdown_a = dropdown.find('a', class_='bulmaio-dropdown-main')
    assert 'more.html' == dropdown_a.attrs['href']
    assert 'More' == dropdown_a.string.strip()
    submenu = dropdown.find('div', class_='navbar-dropdown')
    submenu_entries = submenu.find_all('a', class_='navbar-item')
    assert 2 == len(submenu_entries)
    se0 = submenu_entries[0]
    assert 'more1.html' == se0.attrs['href']
    se0_span = se0.find('span', class_='icon')
    assert 'has-text-link' in se0_span.attrs['class']
    se0_i = se0.find('i')
    assert 'fa-plus' in se0_i.attrs['class']
    se0_strong = se0.find('strong')
    assert 'More1' == se0_strong.string.strip()
    se0_br = se0.find_all('br')
    assert 1 == len(se0_br)

    # Make sure no br on second one
    se1_br = submenu_entries[1].find_all('br')
    assert 0 == len(se1_br)


@pytest.mark.parametrize(
    'page', [['macros_end.html', context_end], ], indirect=True
)
def test_end(page):
    a = page.find_all('a', class_='navbar-item')
    assert 1 == len(a)
    assert 'https://github.com/jgthms/bulma' == a[0].attrs['href']
    icon = a[0].find('i')
    assert 'fa-github-alt' in icon.attrs['class']
