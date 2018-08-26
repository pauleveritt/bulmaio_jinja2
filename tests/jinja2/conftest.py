import pytest
from _pytest.fixtures import FixtureRequest
from bs4 import BeautifulSoup
from jinja2 import (
    ChoiceLoader,
    FileSystemLoader,
    Environment,
    PackageLoader,
)


@pytest.fixture(scope='module')
def template_dir(request):
    return str(request.fspath.join('../templates'))


@pytest.fixture
def env(template_dir):
    loader1 = PackageLoader('bulmaio_jinja2', 'templates')
    loader2 = FileSystemLoader(template_dir)
    loader = ChoiceLoader((loader1, loader2))
    return Environment(loader=loader)


@pytest.fixture
def render(env, request):
    templatename = request.param[0]
    context = request.param[1]()
    template = env.get_template(templatename)
    result = template.render(context)
    soup = BeautifulSoup(result, 'html5lib')
    return soup
