import glob
import os

from flask import Flask, render_template, send_from_directory
from livereload import Server
from livereload.watcher import Watcher

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


def load_content(pagename):
    with open(f'bulmaio_jinja2/content/{pagename}', 'r') as f:
        return f.read()


pages = {
    'index.html': dict(
        template='homepage.html',
        content=load_content('index.html')
    ),
    'documentation.html': dict(
        template='documentation_homepage.html',
        content=load_content('documentation.html')
    ),
    'documentation_overview.html': dict(
        template='documentation.html',
        content=load_content('documentation_overview.html')
    ),
    'documentation_elements_box.html': dict(
        template='documentation.html',
        content=load_content('documentation_elements_box.html')
    ),
}


@app.route('/static/favicons/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/', defaults={'pagename': 'index.html'})
@app.route('/<pagename>')
def hello_world(pagename):
    page = pages.get(pagename)
    context = dict(
        content=page['content'],
        pagename=pagename,
        template=page['template']
    )
    return render_template(page['template'], **context)


class CustomWatcher(Watcher):
    """ Handle recursive globs with Python 3.5+ globbing  """

    paths = [
        '**',
    ]
    root = 'bulmaio_jinja2'

    def is_glob_changed(self, path, ignore=None):
        for f in glob.glob(path, recursive=True):
            if self.is_file_changed(f, ignore):  # pragma: no cover
                return True
        return False


if __name__ == '__main__':
    watcher = CustomWatcher()
    server = Server(app.wsgi_app, watcher=CustomWatcher())
    for p in watcher.paths:
        server.watch(p, ignore=lambda s: '_build' in s)
    server.serve(root=watcher.root)
