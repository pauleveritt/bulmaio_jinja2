import pytest
from bulmaio_jinja2.utils import relative_uri, static_path


@pytest.mark.parametrize(
    'base, to, expected',
    [
        ('index', '_static/css/base.css', '_static/css/base.css'),
        ('about', '_static/css/base.css', '_static/css/base.css'),
        ('a/index', '_static/css/base.css', '../_static/css/base.css'),
        ('a/about', '_static/css/base.css', '../_static/css/base.css'),
        ('a/b/index', '_static/css/base.css', '../../_static/css/base.css'),
        ('a/b/about', '_static/css/base.css', '../../_static/css/base.css'),
    ]
)
def test_relative_uri(base, to, expected):
    result = relative_uri(base, to)

    assert expected == result


@pytest.mark.parametrize(
    'base, to, expected',
    [
        ('index', 'css/base.css', '_static/css/base.css'),
        ('about', 'css/base.css', '_static/css/base.css'),
        ('a/index', 'css/base.css', '../_static/css/base.css'),
        ('a/about', 'css/base.css', '../_static/css/base.css'),
        ('a/b/index', 'css/base.css', '../../_static/css/base.css'),
        ('a/b/about', 'css/base.css', '../../_static/css/base.css'),
    ]
)
def test_static_path(base, to, expected):
    result = static_path('_static', base, to)

    assert expected == result
