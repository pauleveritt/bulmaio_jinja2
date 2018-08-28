from bulmaio_jinja2.base_model import CustomBaseModel
from bulmaio_jinja2.models import Site
from bulmaio_jinja2.navbar.brand.models import NavbarBrand
from bulmaio_jinja2.navbar.end.models import NavbarEnd
from bulmaio_jinja2.navbar.start.models import NavbarStart
from bulmaio_jinja2.page.models import Page


class Navbar(CustomBaseModel):
    brand: NavbarBrand
    start: NavbarStart
    end: NavbarEnd = None

    def update(self, site: Site, page: Page):
        """ Update hrefs and static paths from site/page data """

        self.brand.update(site, page)
        self.start.update(site, page)
        self.end.update(site, page)