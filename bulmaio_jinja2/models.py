from typing import Optional, List

from pydantic import BaseModel


class Breadcrumb(BaseModel):
    label: str
    href: str
    is_active: bool = False


class Tab(BaseModel):
    label: str
    href: str
    is_active: bool = False


class Section(BaseModel):
    label: str
    subheading: str
    href: str
    accent: str
    icon: str


class Page(BaseModel):
    docname: str
    title: str = None
    body: str = None
    subtitle: str = None
    breadcrumbs: Optional[List[Breadcrumb]] = None
    tabs: Optional[List[Tab]] = None
    sections: Optional[List[Section]] = None
    template: str = 'page.html'

