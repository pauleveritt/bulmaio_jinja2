from typing import List

from bulmaio_jinja2.base_model import CustomBaseModel


class FooterLinksGroupMore(CustomBaseModel):
    label: str
    href: str


class FooterLinksEntry(CustomBaseModel):
    label: str
    href: str
    icon: str = None
    subtitle: str = None
    accent: str = None


class FooterLinksGroup(CustomBaseModel):
    label: str
    href: str = None
    more: FooterLinksGroupMore = None
    entries: List[FooterLinksEntry] = []


class FooterLinksColumn(CustomBaseModel):
    groups: List[FooterLinksGroup] = None
    fullsize: bool = False


class FooterLinks(CustomBaseModel):
    columns: List[FooterLinksColumn] = []
