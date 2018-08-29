from typing import List

from bulmaio_jinja2.base_model import CustomBaseModel


class SectionSidebarSubEntry(CustomBaseModel):
    label: str
    href: str
    is_active: bool = False


class SectionSidebarEntry(CustomBaseModel):
    label: str
    href: str
    is_active: bool = False
    is_new: bool = False
    entries: List[SectionSidebarSubEntry] = []


class SectionSidebar(CustomBaseModel):
    entries: List[SectionSidebarEntry] = []
