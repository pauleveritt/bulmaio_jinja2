from typing import List

from bulmaio_jinja2.common.models import BasePage
from bulmaio_jinja2.common.resource_card.models import ResourceCard


class Reference(BasePage):
    entries: List[ResourceCard] = []
