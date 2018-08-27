import pytest

from bulmaio_jinja2.models import Site


@pytest.fixture
def context_social():
    site = Site(
        project_title='Bulma',
        author=dict(
            name='Jeremy',
            website='http://jeremy',
            twitter='jb',
        ),
        footer=dict(
            share=dict(
                twitter=dict(
                    url='http://social',
                    related='user:Some Related'
                )
            )
        )
    )

    return dict(site=site)


@pytest.mark.parametrize(
    'page', [['macros_social.html', context_social], ], indirect=True
)
def test_social(page):
    title = page.find('h4', class_='bio-footer-projectitle')
    strong = title.find('strong')
    assert 'Bulma' == strong.string.strip()
    author = title.find('a')
    assert 'http://jeremy' == author.attrs['href']
    assert 'Jeremy' == author.string.strip()

    # Twitter iframe
    iframe = page.find('a', 'twitter-follow-button')
    assert 'https://twitter.com/jb' == iframe.attrs['href']
    assert '@jb' == iframe.string.strip()
