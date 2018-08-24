from bulmaio_jinja2.models import Site

extensions = [
    'bulmaio_jinja2'
]

html_theme = 'bulmaio_jinja2'
master_doc = 'index'
exclude_patterns = ['_build']

bulmaio_jinja2_siteconfig = Site(
    homepage_url='/index.html',
    logo=dict(
        img_file='images/bulma-logo.png',
        alt='Bulma Logo'
    ),
    title='bulmaio_jinja2',
    favicon='jetbrains_favicon.ico',
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
        ],
        end=dict(
            links=[
                dict(
                    color='333',
                    href='https://github.com/jgthms/bulma',
                    icon='github-alt',
                )
            ]
        )
    ),
    footer=dict(
        links=dict(
            columns=[
                dict(
                    groups=[
                        dict(
                            label='Home',
                            href='https://bulma.io'
                        ),
                        dict(
                            label='Blog',
                            href='/blog.html',
                            more=dict(
                                label='View all posts',
                                href='/all_blog.html'
                            ),
                            entries=[
                                dict(
                                    label='Automatic variables docs',
                                    href='/1.html',
                                )
                            ]
                        ),
                    ]
                ),
                dict(
                    groups=[
                        dict(
                            label='Documentation',
                            href='https://bulma.io'
                        ),
                    ]
                ),

            ]
        )
    )
)
