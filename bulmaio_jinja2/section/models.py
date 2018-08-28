from bulmaio_jinja2.models import BasePage
from bulmaio_jinja2.page.subsections.models import PageSubsections
from bulmaio_jinja2.page.tabs.models import PageTabs


class Section(BasePage):
    subsections: PageSubsections = None
    tabs: PageTabs = None
