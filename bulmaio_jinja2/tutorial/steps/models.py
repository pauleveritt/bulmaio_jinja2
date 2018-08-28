from typing import List

from bulmaio_jinja2.author.models import Author
from bulmaio_jinja2.base_model import CustomBaseModel


class StepReference(CustomBaseModel):
    href: str
    title: str


class Step(CustomBaseModel):
    logo: str = None
    title: str
    href: str
    subtitle: str
    author: Author
    rtype: str
    references: List[StepReference] = None
    duration: str = None
    published: str
