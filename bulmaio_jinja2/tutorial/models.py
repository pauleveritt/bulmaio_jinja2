from bulmaio_jinja2.author.models import Author
from bulmaio_jinja2.common.models import BasePage
from bulmaio_jinja2.sidebar.page.models import PageSidebar
from bulmaio_jinja2.tutorial.steps.models import (
    StepsListing,
    StepsSidebarPanel
)


class TutorialSidebar(PageSidebar):
    steps: StepsSidebarPanel


class Tutorial(BasePage):
    steps: StepsListing


class TutorialPage(BasePage):
    steps: StepsListing
    author: Author = None
    published: str = None
