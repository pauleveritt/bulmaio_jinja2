from dataclasses import dataclass


@dataclass
class PageHeading:
    title: str
    subtitle: str = None

    @classmethod
    def validate(cls, v):
        # do some validation or simply pass through the value
        return v

    @classmethod
    def get_validators(cls):
        yield cls.validate
