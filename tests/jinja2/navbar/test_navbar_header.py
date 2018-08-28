import pytest
from bulmaio_jinja2.navbar.brand.models import NavbarBrand
from bulmaio_jinja2.navbar.end.models import NavbarEnd
from bulmaio_jinja2.navbar.models import Navbar

from bulmaio_jinja2.navbar.start.models import NavbarStart


@pytest.fixture
def context_header():
    navbar_brand = NavbarBrand(
        homepage_href='../../index.html',
        img_src='images/bulma-logo.png',
        alt='Bulma Logo',
        github_url='http://github',
        twitter_url='http://twitter',
    )

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

    navbar_end = NavbarEnd(
        links=[
            dict(
                color='333',
                href='https://github.com/jgthms/bulma',
                icon='github-alt',
            )
        ]
    )
    navbar = Navbar(
        brand=navbar_brand,
        start=navbar_start,
        end=navbar_end
    )

    return dict(navbar=navbar)


@pytest.mark.parametrize(
    'page',
    [['navbar/header.html', context_header], ],
    indirect=True
)
def test_navbar_header(page):
    pass
