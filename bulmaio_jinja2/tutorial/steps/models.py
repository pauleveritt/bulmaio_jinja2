from typing import List

from bulmaio_jinja2.base_model import CustomBaseModel
from bulmaio_jinja2.common.resource_card.models import ResourceCard


class StepsListing(CustomBaseModel):
    entries: List[ResourceCard] = []


class StepsSidebarPanelEntry(CustomBaseModel):
    title: str
    subtitle: str
    href: str
    is_active: bool = False


class StepsSidebarPanel(CustomBaseModel):
    entries: List[StepsSidebarPanelEntry] = []
