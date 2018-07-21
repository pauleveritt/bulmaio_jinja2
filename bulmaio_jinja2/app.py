import os

from flask import Flask, render_template, send_from_directory, make_response

from bulmaio_jinja2.content import (
    get_pages,
    navbar_start,
)

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/bulmaio.map')
def file_downloads():
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
def hello_world(pagename):
    pages = get_pages()
    page = pages.get(pagename)
    context = dict(
        content=page['content'],
        pagename=pagename,
        template=page['template'],
        navbar_start=navbar_start
    )

    return render_template(page['template'], **context)
