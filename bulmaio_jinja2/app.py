import os

from flask import Flask, render_template, send_from_directory

from bulmaio_jinja2.content import get_pages

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


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
        template=page['template']
    )

    return render_template(page['template'], **context)
