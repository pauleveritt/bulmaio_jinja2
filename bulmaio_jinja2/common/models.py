from typing import Optional

from bulmaio_jinja2.base_model import CustomBaseModel
from bulmaio_jinja2.page.breadcrumbs.models import PageBreadcrumbs
from bulmaio_jinja2.page.heading.models import PageHeading


class SocialMedia(CustomBaseModel):
    twitter: str = None
    github: str = None


class License(CustomBaseModel):
    name: str
    url: str


class BasePage(CustomBaseModel):
    docname: str
    title: str = None
    body: str = None
    subtitle: str = None
    template: Optional[str] = 'page.html'
    breadcrumbs: PageBreadcrumbs = None
    heading: PageHeading = None
