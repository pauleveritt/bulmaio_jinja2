from collections import UserDict
from dataclasses import dataclass
from os.path import join
from pathlib import Path

from yaml import Loader, load

cwd = Path(__file__).parents[0]


def load_yaml(filename):
    fn = join(cwd, filename + '.yaml')
    with open(fn, 'r') as f:
        data = load(f, Loader=Loader)
        return data


@dataclass
class Page:
    docname: str
    title: str
    template: str = 'documentation.html'

    @property
    def content(self):
        fn = join(cwd, self.docname)
        with open(fn, 'r') as f:
            return f.read()


class Pages(UserDict):
    def add(self, page: Page):
        self.data[page.docname] = page

    def load_pages(self):
        pages = load_yaml('pages')
        for page_data in pages:
            page = Page(**page_data)
            self.add(page)
