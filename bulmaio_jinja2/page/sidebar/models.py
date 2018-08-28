from bulmaio_jinja2.author.models import Author
from bulmaio_jinja2.base_model import CustomBaseModel


class SidebarPublished(CustomBaseModel):
    published_date: str = None
    published_time: str = None
    author: Author = None


class Sidebar(CustomBaseModel):
    published: SidebarPublished
