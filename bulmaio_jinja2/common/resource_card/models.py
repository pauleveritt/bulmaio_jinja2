from typing import List

from bulmaio_jinja2.author.models import Author
from bulmaio_jinja2.base_model import CustomBaseModel


class ResourceCardLogo(CustomBaseModel):
    href: str = None


class ResourceCardReference(CustomBaseModel):
    href: str
    title: str


class ResourceCard(CustomBaseModel):
    href: str
    title: str
    subtitle: str = None
    logo: ResourceCardLogo
    author: Author = None
    rtype: str
    references: List[ResourceCardReference] = None
    duration: str = None
    published: str
