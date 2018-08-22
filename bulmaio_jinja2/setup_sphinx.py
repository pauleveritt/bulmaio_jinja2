import inspect
import os

from sphinx.application import Sphinx

import bulmaio_jinja2
from sphinx.jinja2glue import SphinxFileSystemLoader


def html_context(app, pagename, templatename, context, doctree):
    context['site'] = app.config.bulmaio_jinja2_siteconfig


def add_template_dir(app: Sphinx):
    """ Called on builderinit, let's add the template subdir """

    # Usually Sphinx themes put their templates in the root,
    # where the theme.conf and __init__.setup reside. That's
    # dumb, plus, we want to register these templates for use
    # even if a different theme is used.

    template_bridge = app.builder.templates
    t = os.path.join(os.path.dirname(inspect.getfile(bulmaio_jinja2)),
                     'templates')
    template_bridge.loaders.append(SphinxFileSystemLoader(t))
    # m = os.path.join(os.path.dirname(inspect.getfile(bulmaio_jinja2)),
    #                  'templates/macros')
    # template_bridge.loaders.append(SphinxFileSystemLoader(m))


def setup_sphinx(app: Sphinx):
    app.add_config_value(
        'bulmaio_jinja2_siteconfig', None, 'html'
    )

    app.add_html_theme(
        'bulmaio_jinja2',
        os.path.abspath(os.path.dirname(__file__))
    )

    app.connect('html-page-context', html_context)
    app.connect('builder-inited', add_template_dir)

    return dict(
        parallel_read_safe=True
    )
