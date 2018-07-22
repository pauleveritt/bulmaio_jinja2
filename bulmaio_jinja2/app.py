import os

from flask import Flask, render_template, send_from_directory, make_response

from bulmaio_jinja2.content import (
    Pages,
    load_yaml
)

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
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/', defaults={'pagename': 'index.html'})
@app.route('/<pagename>')
def page_view(pagename):
    pages = Pages()
    pages.load_pages()
    navbar = load_yaml('navbar')
    page = pages.get(pagename)
    context = dict(
        page=page,
        navbar=navbar
    )

    return render_template(page.template, **context)
