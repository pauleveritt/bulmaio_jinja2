from typing import List

from bulmaio_jinja2.base_model import CustomBaseModel


class PageSubsection(CustomBaseModel):
    label: str
    subtitle: str
    href: str
    accent: str
    icon: str


class PageSubsections(CustomBaseModel):
    entries: List[PageSubsection] = []
