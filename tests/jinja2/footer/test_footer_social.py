import pytest
from bulmaio_jinja2.footer.social.models import FooterSocial


@pytest.fixture
def context_social():
    footer_social = FooterSocial(
        project=dict(
            title='Bulma',
            author=dict(
                name='Jeremy',
                website='http://jeremy',
                twitter='jb',
            ),
            license=dict(
                name='MIT',
                href='https://opensource.org/licenses/mit-license.php'
            ),
            github=dict(
                user='',
                repo='',
            )
        ),
        site=dict(
            title='Bulma',
            license=dict(
                name='MIT',
                href='https://opensource.org/licenses/mit-license.php'
            ),
            author=dict(
                name='Jeremy',
                website='http://jeremy',
                twitter='jb',
            ),
        ),
        share=dict(
            twitter=dict(
                url='http://social',
                related='user:Some Related'
            )
        )
    )

    return dict(footer_social=footer_social)


@pytest.mark.parametrize(
    'page',
    [['test_footer_social.html', context_social], ],
    indirect=True
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
