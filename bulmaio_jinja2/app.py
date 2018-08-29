import os
from pathlib import Path

from bulmaio_jinja2.footer.models import Footer
from bulmaio_jinja2.navbar.models import Navbar
from bulmaio_jinja2.sample import Pages
from bulmaio_jinja2.site.models import Site
from bulmaio_jinja2.utils import load_yaml
from flask import Flask, render_template, send_from_directory, make_response
from jinja2 import ChoiceLoader, PackageLoader

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_loader = ChoiceLoader([
    PackageLoader('bulmaio_jinja2', 'templates'),
    PackageLoader('bulmaio_jinja2', '.'),
])

cwd = Path(__file__).parents[0]


@app.route('/bulmaio_jinja2.map')
def sourcemaps():
    # Likely a problem with Parcel encoding an absolute path in the .js
    # to point at the .map
    headers = {}
    with open('bulmaio_jinja2/static/bulmaio_jinja2.map', 'r') as f:
        body = f.read()
    return make_response((body, headers))


@app.route('/favicon.ico')
@app.route('/static/favicons/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static', 'favicons'),
        'bulma-logo.png',
        mimetype='image/vnd.microsoft.icon')


@app.route('/', defaults={'pagename': 'index.html'})
@app.route('/<pagename>')
def page_view(pagename):
    # Make a Site with a Footer
    site = Site(**load_yaml('sample/site', base_dir=cwd))
    site.static_dirname = 'static/'  # Don't use Sphinx name

    # Get some globals. Jam them in here so that livereload will get them,
    # slows down requests for development, but that's ok.
    pages = Pages()
    pages.load_pages()

    # Get this page
    page = pages.get(pagename)

    # Make a navbar with site-specific and page-specific data
    navbar = Navbar(**load_yaml('sample/navbar', base_dir=cwd))
    navbar.update(site, page)

    # Make a footer
    footer = Footer(**load_yaml('sample/footer', base_dir=cwd))

    # Make a context
    context = dict(
        site=site,
        page=page,
        navbar=navbar,
        footer=footer
    )

    # One last thing....set the correct is_active on the section_sidebar
    try:
        active_category = [
            category
            for category in site.section_sidebar.entries
            if category.href[1:-6] in page.docname
        ]
    except AttributeError:
        pass
    if active_category:
        active_category[0].is_active = True

    return render_template(page.template, **context)
