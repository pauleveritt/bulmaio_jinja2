from typing import List

from bulmaio_jinja2.base_model import CustomBaseModel


class PageBreadcrumb(CustomBaseModel):
    label: str
    href: str
    is_active: bool = False


class PageBreadcrumbPrevNext(CustomBaseModel):
    href: str
    title: str


class PageBreadcrumbs(CustomBaseModel):
    entries: List[PageBreadcrumb] = []
    prev: PageBreadcrumbPrevNext = None
    next: PageBreadcrumbPrevNext = None
