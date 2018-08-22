from bulmaio_jinja2.setup_sphinx import (
    html_context,
    setup_sphinx,
)


def test_imports():
    assert 'html_context' == html_context.__name__
    assert 'setup_sphinx' == setup_sphinx.__name__

