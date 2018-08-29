from bulmaio_jinja2.author.models import Author
from bulmaio_jinja2.common.models import BasePage
from bulmaio_jinja2.page.tabs.models import PageTabs


class Page(BasePage):
    tabs: PageTabs = None
    author: Author = None
    published: str = None
