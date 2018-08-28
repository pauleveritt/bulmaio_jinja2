from typing import List

from bulmaio_jinja2.base_model import CustomBaseModel
from bulmaio_jinja2.models import Site, Page


class NavbarEndLink(CustomBaseModel):
    color: str
    href: str
    icon: str


class NavbarEndButton(CustomBaseModel):
    accent: str
    href: str
    label: str


class NavbarEnd(CustomBaseModel):
    links: List[NavbarEndLink] = []
    buttons: List[NavbarEndButton] = []

    def update(self, site: Site, page: Page):
        """ Update hrefs and static paths from site/page data """

        pass
