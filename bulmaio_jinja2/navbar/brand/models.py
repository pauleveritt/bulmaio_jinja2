from bulmaio_jinja2.base_model import CustomBaseModel
from bulmaio_jinja2.page.models import Page
from bulmaio_jinja2.site.models import Site


class NavbarBrand(CustomBaseModel):
    homepage_href: str
    img_src: str = None
    alt: str = None
    github_url: str = None
    twitter_url: str = None

    def update(self, site: Site, page: Page):
        """ Update hrefs and static paths from site/page data """

        docname = page.docname
        self.img_src = site.static_path(docname, self.img_src)
