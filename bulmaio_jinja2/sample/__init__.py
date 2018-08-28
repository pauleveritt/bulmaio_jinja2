from collections import UserDict
from os.path import join
from pathlib import Path

from bulmaio_jinja2.page.models import Page
from bulmaio_jinja2.section.models import Section
from bulmaio_jinja2.tutorial.models import Tutorial
from bulmaio_jinja2.utils import load_yaml
from pydantic import ValidationError

cwd = Path(__file__).parents[0]

klasses = {
    'page.html': Page,
    'section.html': Section,
    'homepage.html': Page,
    'tutorial.html': Tutorial
}


class Pages(UserDict):
    def add(self, page: Page):
        self.data[page.docname] = page

    def load_pages(self):
        pages = load_yaml('pages', base_dir=cwd)
        for page_data in pages:
            klass = klasses[page_data['template']]
            try:
                page = klass(**page_data)
            except ValidationError:
                raise TypeError(page_data['docname'], klass)
            self.add(page)

            # Now add the .html content as page.body
            fn = join(cwd, page.docname)
            with open(fn, 'r') as f:
                page.body = f.read()
