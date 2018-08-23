import os

from bulmaio_jinja2.models import (
    Navbar,
    Site,
    Footer
)
from bulmaio_jinja2.sample import (
    Pages,
    load_yaml
)
from flask import Flask, render_template, send_from_directory, make_response

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/bulmaio.map')
def sourcemaps():
    # Likely a problem with Parcel encoding an absolute path in the .js
    # to point at the .map
    headers = {}
    with open('bulmaio_jinja2/static/js/bulmaio.map', 'r') as f:
        body = f.read()
    return make_response((body, headers))


@app.route('/static/favicons/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static', 'favicons'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon')


@app.route('/', defaults={'pagename': 'index.html'})
@app.route('/<pagename>')
def page_view(pagename):
    # Get some globals. Jam them in here so that livereload will get them,
    # slows down requests for development, but that's ok.
    pages = Pages()
    pages.load_pages()

    # Make a Site with a Navbar and a Footer
    site = Site(**load_yaml('site'))
    site.navbar = Navbar(**load_yaml('navbar'))
    site.footer = Footer(**load_yaml('footer'))
    site.static_dirname = 'static/'  # Don't use Sphinx name

    # Get this page and make a context
    page = pages.get(pagename)
    context = dict(
        site=site,
        page=page,
    )

    return render_template(page.template, **context)
