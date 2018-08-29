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
