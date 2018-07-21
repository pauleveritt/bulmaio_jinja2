import glob

from flask import Flask, render_template
from livereload import Server
from livereload.watcher import Watcher

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/<pagename>')
@app.route('/')
def hello_world(pagename=None):
    if pagename is None:
        pagename = 'index.html'
    return render_template(pagename)


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
