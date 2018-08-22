import os

from sphinx.application import Sphinx


def html_context(app, pagename, templatename, context, doctree):
    context['site'] = app.config.bulmaio_jinja2_siteconfig


def setup_sphinx(app: Sphinx):
    app.add_config_value(
        'bulmaio_jinja2_siteconfig', None, 'html'
    )

    app.add_html_theme(
        'bulmaio_jinja2',
        os.path.abspath(os.path.dirname(__file__))
    )

    app.connect('html-page-context', html_context)

    return dict(
        parallel_read_safe=True
    )

