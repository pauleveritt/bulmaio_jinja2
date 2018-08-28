import pytest

from bulmaio_jinja2.navbar.start.models import NavbarStart


@pytest.fixture
def context_start():
    navbar_start = NavbarStart(
        entries=[
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

    return dict(navbar_start=navbar_start)


@pytest.mark.parametrize(
    'page',
    [['test_navbar_start.html', context_start], ],
    indirect=True
)
def test_navbar_start(page):
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
    dropdown_a = dropdown.find('a', class_='bio-dropdown-main')
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
    se0_description = se0.find('span', class_='bio-dropdown-description')
    assert 'More1 Description' == se0_description.string.strip()
    se0_br = se0.find_all('br')
    assert 1 == len(se0_br)

    # Make sure no br on second one
    se1_br = submenu_entries[1].find_all('br')
    assert 0 == len(se1_br)
