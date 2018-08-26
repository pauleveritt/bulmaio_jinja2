from bulmaio_jinja2.sphinx import (
    add_template_dir,
    copy_static,
    inject_page,
    inject_site,
    setup_sphinx,
)


def test_imports():
    assert 'add_template_dir' == add_template_dir.__name__
    assert 'copy_static' == copy_static.__name__
    assert 'inject_page' == inject_page.__name__
    assert 'inject_site' == inject_site.__name__
    assert 'setup_sphinx' == setup_sphinx.__name__
