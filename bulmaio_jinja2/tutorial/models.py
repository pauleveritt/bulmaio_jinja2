from bulmaio_jinja2.models import BasePage
from bulmaio_jinja2.page.sidebar.models import Sidebar
from bulmaio_jinja2.tutorial.steps.models import (
    StepsListing,
    StepsSidebarPanel
)


class TutorialSidebar(Sidebar):
    steps: StepsSidebarPanel


class Tutorial(BasePage):
    steps: StepsListing
    sidebar: TutorialSidebar
