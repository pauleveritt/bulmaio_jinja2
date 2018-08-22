from bulmaio_jinja2.app import (
    sourcemaps,
    favicon,
    page_view,
)


def test_imports():
    assert 'sourcemaps' == sourcemaps.__name__
    assert 'favicon' == favicon.__name__
    assert 'page_view' == page_view.__name__

