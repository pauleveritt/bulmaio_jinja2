import pytest


def test_environment(env):
    loaders = env.loader.loaders

    # Test the package loader
    loader1 = loaders[1]
    module_path = loader1.provider.module_path
    assert module_path.endswith('bulmaio_jinja2')
    package_path = loader1.package_path
    assert 'templates' == package_path

    # Test the local test templates loader
    loader2 = loaders[2]
    searchpath = loader2.searchpath[0]
    assert searchpath.endswith('templates')


@pytest.fixture
def context1():
    return dict(name='World')


@pytest.mark.parametrize(
    'page',
    [
        ['hello.html', context1],
    ],
    indirect=True
)
def test_rendering(page):
    h1 = page.find('h1').string
    assert 'Hello World' == h1
