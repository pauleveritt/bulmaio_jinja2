from bulmaio_jinja2 import SiteConfig

extensions = [
    'bulmaio_jinja2'
]

html_theme = 'bulmaio_jinja2'
html_title = 'Bulmaio Theme Test'
master_doc = 'index'
exclude_patterns = ['_build']

bulmaio_jinja2_siteconfig = SiteConfig(
    title='PyCharm Guide',
    logo=dict(
        img_file='PyCharm_Logo.svg.png',
        alt='Kaybee Logo Alt'
    ),
    copyright='2018, All Rights Reserved',
    favicon='jetbrains_favicon.ico',
    social_media=dict(
        twitter='xxx',
        github='xxx'
    ),
    description='Extensible Knowledge Base for Static Sites',
    navbar=dict(
        start=[
            # dict(
            #     css_class='documentation',
            #     accent='primary',
            #     label='PyCharm Guide',
            #     href='/'
            # ),
            dict(
                css_class='documentation',
                accent='primary',
                icon='book',
                label='Learn',
                href='/learn/'
            ),
            dict(
                css_class='blog',
                accent='rss',
                icon='rss',
                label='News',
                href='/news.html'
            )
        ],
        end=dict(
            links=[
                dict(
                    color='333',
                    href='github',
                    icon='github-alt',
                ),
                dict(
                    color='55acee',
                    href='twitter',
                    icon='twitter',
                ),
            ],
            buttons=[
                dict(
                    accent='primary',
                    href='xxx',
                    label='Search'
                ),
                dict(
                    accent='danger',
                    href='xxx',
                    label='Participate'
                ),

            ]
        )
    ),
    footer=dict(
        links=dict(
            columns=[
                # Column 1
                dict(
                    groups=[
                        # Group 1
                        dict(
                            label='Home',
                            href='/x',
                        ),
                        # Group 2
                        dict(
                            label='Blog',
                            href='/x',
                            more=dict(
                                label='View all posts',
                                href='/x'
                            ),
                            entries=[
                                dict(
                                    label='Automatic variables docs',
                                    href='/x',
                                ),
                                dict(
                                    label='Migrating to v0.7.0',
                                    href='/x',
                                ),
                                dict(
                                    label='Website redesign',
                                    href='/x',
                                ),
                            ]
                        ),
                    ]
                ),
                # Column 2
                dict(
                    groups=[
                        # Group 1
                        dict(
                            label='Documentation',
                            href='/x',
                            entries=[
                                dict(
                                    label='Overview',
                                    href='/x',
                                ),
                                dict(
                                    label='Customize',
                                    href='/x',
                                ),
                                dict(
                                    label='Modifiers',
                                    href='/x',
                                ),
                            ]
                        ),
                    ]
                ),
                # Column 3
                dict(
                    fullsize=True,
                    groups=[
                        dict(
                            label='More',
                            href='/x',
                            entries=[
                                dict(
                                    label='Expo',
                                    icon='star',
                                    accent='star',
                                    subtitle='Official Bulma showcase',
                                    href='/x'
                                ),
                                dict(
                                    label='Love',
                                    icon='heart',
                                    accent='danger',
                                    subtitle='Fans of Bulma around the world',
                                    href='/x'
                                ),
                                dict(
                                    label='Bulma start',
                                    icon='rocket',
                                    accent='success',
                                    subtitle='A tiny npm package to get '
                                             'started',
                                    href='/x'
                                ),
                            ]
                        )
                    ]
                ),
            ]
        )
    )
)
