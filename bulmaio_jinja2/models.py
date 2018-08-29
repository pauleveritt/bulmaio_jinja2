from bulmaio_jinja2.author.models import Author
from bulmaio_jinja2.base_model import CustomBaseModel
from bulmaio_jinja2.footer.models import Footer
from bulmaio_jinja2.section.sidebar.models import SectionSidebar
from bulmaio_jinja2.utils import static_path


class SocialMedia(CustomBaseModel):
    twitter: str = None
    github: str = None


class License(CustomBaseModel):
    name: str
    url: str


class Site(CustomBaseModel):
    homepage_url: str = '/'
    title: str = None
    social_media: SocialMedia = None
    project_title: str = None
    author: Author = None
    copyright: str = 'All Rights Reserved'
    feed_url: str = ''
    favicon: str = None
    is_debug = False
    software_license: License = None
    website_license: License = None
    description: str = None
    footer: Footer = None
    static_dirname: str = '_static/'
    section_sidebar: SectionSidebar = None

    def static_path(self, docname, other):
        return static_path(self.static_dirname, docname, other)
