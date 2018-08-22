from os import path


def setup(app):
    app.add_html_theme(
        'bulmaio_jinja2',
        path.abspath(path.dirname(__file__))
    )
