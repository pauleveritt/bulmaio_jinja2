import inspect
import os
from os import path
from typing import Optional

import bulmaio_jinja2
from bulmaio_jinja2.models import Page
from docutils import nodes
from docutils.nodes import Node
from sphinx.application import Sphinx
from sphinx.util import relative_uri
from sphinx.util.fileutil import copy_asset


def get_rst_title(rst_doc: Node) -> Optional[str]:
    """ Given some RST, extract what docutils thinks is the title """

    if rst_doc:
        for title in rst_doc.traverse(nodes.title):
            return title.astext()

    return None


def inject_site(app, pagename, templatename, context, doctree):
    sc = app.config.bulmaio_jinja2_siteconfig
    t = type(sc)
    context['site'] = app.config.bulmaio_jinja2_siteconfig


def inject_page(app, pagename, templatename, context, doctree):
    # This theme expects all values to come in through
    # validated models. No more globals. So extract the
    # page-specific stuff into an instance
    if doctree is None:
        pass
    title = get_rst_title(doctree)
    body = context.get('body', '')  # genindex has no body

    # Make a page
    page = Page(
        docname=pagename,
        title=title,
        body=body
    )

    # Make some breadcrumbs
    root_href = relative_uri(pagename, 'index') + '.html'
    breadcrumbs = [dict(label='Home', href=root_href)]
    parents = context['parents']
    for parent in parents:
        breadcrumbs.append(
            dict(
                label=parent['title'],
                href=parent['link']
            )
        )
    page.breadcrumbs = breadcrumbs
    context['page'] = page


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


def copy_static(app: Sphinx):
    """ When used in another theme, copy static CSS etc. to _static """

    theme_name = app.config.html_theme
    if theme_name != 'bulmaio_jinja2':
        source = os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'static')
        )
        dest = os.path.join(app.builder.outdir, '_static')
        copy_asset(source, dest)

    if 0:
        # this is to make the function a generator
        # and make work for Sphinx 'html-collect-pages'
        yield


def setup_sphinx(app: Sphinx):
    app.add_config_value(
        'bulmaio_jinja2_siteconfig', None, 'html'
    )

    app.add_html_theme(
        'bulmaio_jinja2',
        os.path.abspath(os.path.dirname(__file__))
    )

    app.connect('builder-inited', add_template_dir)
    app.connect('html-collect-pages', copy_static)
    app.connect('html-page-context', inject_site)
    app.connect('html-page-context', inject_page)


    return dict(
        parallel_read_safe=True
    )
