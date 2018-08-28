from bulmaio_jinja2.utils import static_path
from pydantic import BaseModel


class CustomBaseModel(BaseModel):
    class Config:
        ignore_extra = False

    def static_path(self, docname, other):
        return static_path(docname, other)
