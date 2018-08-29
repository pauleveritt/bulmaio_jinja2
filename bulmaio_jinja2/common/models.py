from bulmaio_jinja2.base_model import CustomBaseModel
from bulmaio_jinja2.page.breadcrumbs.models import PageBreadcrumbs
from bulmaio_jinja2.page.heading.models import PageHeading


class BasePage(CustomBaseModel):
    docname: str
    title: str = None
    body: str = None
    subtitle: str = None
    template: str = 'page.html'
    breadcrumbs: PageBreadcrumbs = None
    heading: PageHeading = None
