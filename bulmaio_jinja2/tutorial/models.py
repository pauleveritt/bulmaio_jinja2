from typing import List

from bulmaio_jinja2.author.models import Author
from bulmaio_jinja2.common.models import BasePage
from bulmaio_jinja2.common.resource_card.models import ResourceCard
from bulmaio_jinja2.sidebar.page.models import PageSidebar
from bulmaio_jinja2.tutorial.steps.models import (
    StepsListing,
    StepsSidebarPanel
)


class TutorialSidebar(PageSidebar):
    steps: StepsSidebarPanel


class Tutorial(BasePage):
    entries: List[ResourceCard] = []
    author: Author = None
    published: str = None


class TutorialPage(BasePage):
    steps: StepsListing
    author: Author = None
    published: str = None
