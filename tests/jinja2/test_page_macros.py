import pytest

from bulmaio_jinja2.models import Page, Site


@pytest.fixture
def context_no_published():
    page = Page(
        docname='about'
    )
    return dict(page=page)


@pytest.fixture
def context_published():
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
        prev=dict(
            title='Previous Page',
            href='/previous.html'
        ),
        next=dict(
            title='Next Page',
            href='/next.html'
        ),
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
        ],
        subsections=[
            dict(
                label='Start',
                subtitle='Start <em>Subtitle</em>',
                href='/start.html',
                accent='danger',
                icon='fas fa-rocket'
            ),
            dict(
                label='Classes',
                subtitle='Classes Subtitle',
                href='/classes.html',
                accent='link',
                icon='fas fa-css3'
            ),
        ]
    )
    return dict(page=page)


# @pytest.mark.parametrize(
#     'page',
#     [['macros_page_sidebar_published.html', context_no_published], ],
#     indirect=True
# )
# def test_no_published(page):
#     bcs = page.find_all('div', class_='bd-breadcrumb')
#     assert 0 == len(bcs)
#
#
# @pytest.mark.parametrize(
#     'page',
#     [['macros_page_sidebar_published.html', context_published], ],
#     indirect=True
# )
# def test_published(page):
#     bcs = page.find_all('div', class_='bd-breadcrumb')
#     assert 1 == len(bcs)
