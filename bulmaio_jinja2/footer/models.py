from bulmaio_jinja2.base_model import CustomBaseModel
from bulmaio_jinja2.footer.links.models import FooterLinks
from bulmaio_jinja2.footer.social.models import FooterSocial
from bulmaio_jinja2.page.models import Page
from bulmaio_jinja2.site.models import Site


class Footer(CustomBaseModel):
    social: FooterSocial = None
    links: FooterLinks = None

    def update(self, site: Site, page: Page):
        """ Update hrefs and static paths from site/page data """

        pass
