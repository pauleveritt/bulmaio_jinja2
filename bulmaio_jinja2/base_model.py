from pydantic import BaseModel


class CustomBaseModel(BaseModel):
    class Config:
        ignore_extra = False

