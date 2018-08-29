from typing import List

from bulmaio_jinja2.author.models import Author
from bulmaio_jinja2.base_model import CustomBaseModel


class SidebarPublished(CustomBaseModel):
    published_date: str = None
    published_time: str = None
    author: Author = None


class SidebarPrevNextItem(CustomBaseModel):
    href: str
    title: str


class SidebarPrevNext(CustomBaseModel):
    prev: SidebarPrevNextItem = None
    next: SidebarPrevNextItem = None


class SidebarReference(CustomBaseModel):
    label: str
    href: str


class SidebarReferenceGroup(CustomBaseModel):
    reftype: str
    entries: List[SidebarReference]


class SidebarReferences(CustomBaseModel):
    entries: List[SidebarReferenceGroup] = []


class Sidebar(CustomBaseModel):
    published: SidebarPublished
    prev_next: SidebarPrevNext
    references: SidebarReferences
