"""

Resolve paths in the local app.

Systems (Sphinx, the devserver Flask app) need a way to resolve
relative paths to documents and particularly static assets.

Provide a callable for static path resolution.
"""
from bulmaio_jinja2.utils import static_path


class Resolver:
    def __init__(self, static_dirname: str, docname: str):
        # Sometims _static, sometimes static...let the Site pass it in
        self.static_dirname = static_dirname
        self.docname = docname

    def __call__(self, target: str, is_static: int = 0):
        """ Given the current docname and the thing to link to, resolve """

        return static_path(self.static_dirname, self.docname, target)
