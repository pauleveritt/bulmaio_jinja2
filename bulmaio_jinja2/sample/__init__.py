from collections import UserDict
from os.path import join
from pathlib import Path

from bulmaio_jinja2.models import Page
from yaml import Loader, load

cwd = Path(__file__).parents[0]


def load_yaml(filename):
    fn = join(cwd, filename + '.yaml')
    with open(fn, 'r') as f:
        data = load(f, Loader=Loader)
        return data


class Pages(UserDict):
    def add(self, page: Page):
        self.data[page.docname] = page

    def load_pages(self):
        pages = load_yaml('pages')
        for page_data in pages:
            page = Page(**page_data)
            self.add(page)

            # Now add the .html content as page.body
            fn = join(cwd, page.docname)
            with open(fn, 'r') as f:
                page.body = f.read()
