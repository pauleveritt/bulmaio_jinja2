import pytest
from _pytest.fixtures import SubRequest
from bs4 import BeautifulSoup
from jinja2 import (
    ChoiceLoader,
    FileSystemLoader,
    Environment,
    PackageLoader,
)


@pytest.fixture()
def template_dir(request):
    return str(request.fspath.join('../templates'))


@pytest.fixture
def env(template_dir):
    loader1 = PackageLoader('bulmaio_jinja2', '.')
    loader2 = PackageLoader('bulmaio_jinja2', 'templates')
    loader3 = FileSystemLoader(template_dir)
    loader = ChoiceLoader((loader1, loader2, loader3))
    return Environment(loader=loader)


@pytest.fixture
def page(env, request: SubRequest):
    template_name = request.param[0]
    context = request.param[1]()
    template = env.get_template(template_name)
    result = template.render(context)
    soup = BeautifulSoup(result, 'html5lib')
    return soup
