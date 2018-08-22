from bulmaio_jinja2.livereload import (
    CustomWatcher,
    main,
)


def test_imports():
    assert 'CustomWatcher' == CustomWatcher.__name__
    assert 'main' == main.__name__
