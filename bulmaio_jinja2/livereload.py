import glob

from livereload import Server
from livereload.watcher import Watcher

from bulmaio_jinja2.app import app


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


def main():
    watcher = CustomWatcher()
    server = Server(app.wsgi_app, watcher=CustomWatcher())
    for p in watcher.paths:
        server.watch(p, ignore=lambda s: '_build' in s)
    server.serve(root=watcher.root)


if __name__ == '__main__':
    main()
