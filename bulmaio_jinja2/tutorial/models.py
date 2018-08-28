from typing import List

from bulmaio_jinja2.models import BasePage
from bulmaio_jinja2.tutorial.steps.models import Step


class Tutorial(BasePage):
    steps: List[Step] = None
