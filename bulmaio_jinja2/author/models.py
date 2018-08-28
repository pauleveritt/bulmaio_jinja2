from bulmaio_jinja2.base_model import CustomBaseModel


class Author(CustomBaseModel):
    name: str
    website: str = None
    twitter: str = None
    thumbnail_url: str = None


