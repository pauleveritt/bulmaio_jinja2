from typing import List

from bulmaio_jinja2.base_model import CustomBaseModel
from bulmaio_jinja2.models import Site, Page


class NavbarStartSubEntry(CustomBaseModel):
    css_class: str = None
    accent: str = None
    icon: str = None
    label: str
    description: str = None
    label_narrow: str = None
    href: str


class NavbarStartEntry(CustomBaseModel):
    css_class: str = None
    accent: str = None
    icon: str = None
    label: str
    label_narrow: str = None
    href: str
    submenu: List[NavbarStartSubEntry] = None


class NavbarStart(CustomBaseModel):
    entries: List[NavbarStartEntry] = []

    def update(self, site: Site, page: Page):
        """ Update hrefs and static paths from site/page data """

        pass