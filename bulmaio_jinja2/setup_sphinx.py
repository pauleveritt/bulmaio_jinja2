import inspect
import os
from typing import Optional

import bulmaio_jinja2
from bulmaio_jinja2.models import Page
from docutils import nodes
from docutils.nodes import Node
from sphinx.application import Sphinx


def get_rst_title(rst_doc: Node) -> Optional[str]:
    """ Given some RST, extract what docutils thinks is the title """

    if rst_doc:
        for title in rst_doc.traverse(nodes.title):
            return title.astext()

    return None


def html_context(app, pagename, templatename, context, doctree):
    context['site'] = app.config.bulmaio_jinja2_siteconfig

    # This theme expects all values to come in through
    # validated models. No more globals. So extract the
    # page-specific stuff into an instance
    if doctree is None:
        pass
    title = get_rst_title(doctree)
    body = context.get('body', '')  # genindex has no body

    context['page'] = Page(
        docname=pagename,
        title=title,
        body=body
    )


def add_template_dir(app: Sphinx):
    """ Called on builderinit, let's add the template subdir """

    # Usually Sphinx themes put their templates in the root,
    # where the theme.conf and __init__.setup reside. That's
    # dumb, plus, we want to register these templates for use
    # even if a different theme is used.

    template_bridge = app.builder.templates
    t = os.path.join(os.path.dirname(inspect.getfile(bulmaio_jinja2)),
                     'templates')
    template_bridge.loaders[0].searchpath.append(t)


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
