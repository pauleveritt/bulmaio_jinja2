import os

from bulmaio_jinja2.site_config import SiteConfig


def html_context(app, pagename, templatename, context, doctree):
    context['site'] = app.config.bulmaio_jinja2_siteconfig


def setup(app):
    app.add_config_value(
        'bulmaio_jinja2_siteconfig', SiteConfig(), 'html'
    )

    app.add_html_theme(
        'bulmaio_jinja2',
        os.path.abspath(os.path.dirname(__file__))
    )

    app.connect('html-page-context', html_context)

    return dict(
        parallel_read_safe=True
    )
