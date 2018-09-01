from bulmaio_jinja2.author.models import Author
from bulmaio_jinja2.base_model import CustomBaseModel
from bulmaio_jinja2.common.models import SocialMedia, License


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
    static_dirname: str = '_static/'
