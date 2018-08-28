from bulmaio_jinja2.base_model import CustomBaseModel


class PageHeading(CustomBaseModel):
    title: str
    subtitle: str = None