from typing import List

from bulmaio_jinja2.base_model import CustomBaseModel


class PageTab(CustomBaseModel):
    label: str
    href: str
    is_active: bool = False


class PageTabs(CustomBaseModel):
    entries: List[PageTab] = []
