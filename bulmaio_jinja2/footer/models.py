from bulmaio_jinja2.base_model import CustomBaseModel
from bulmaio_jinja2.footer.links.models import FooterLinks
from bulmaio_jinja2.footer.social.models import FooterSocial


class Footer(CustomBaseModel):
    social: FooterSocial = None
    links: FooterLinks = None
