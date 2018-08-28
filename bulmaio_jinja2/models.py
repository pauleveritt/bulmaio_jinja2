from typing import List
from typing import Optional

from bulmaio_jinja2.base_model import CustomBaseModel
from bulmaio_jinja2.footer.social.models import FooterSocial
from bulmaio_jinja2.utils import static_path


class Author(CustomBaseModel):
    name: str
    website: str = None
    twitter: str = None
    thumbnail_url: str = None


class Breadcrumb(CustomBaseModel):
    label: str
    href: str
    is_active: bool = False


class Tab(CustomBaseModel):
    label: str
    href: str
    is_active: bool = False


class Subsection(CustomBaseModel):
    label: str
    subtitle: str
    href: str
    accent: str
    icon: str


class PrevNext(CustomBaseModel):
    href: str
    title: str


class StepReference(CustomBaseModel):
    href: str
    title: str


class Step(CustomBaseModel):
    logo: str = None
    title: str
    href: str
    subtitle: str
    author: Author
    rtype: str
    references: List[StepReference] = None
    duration: str = None
    published: str


class Page(CustomBaseModel):
    docname: str
    title: str = None
    body: str = None
    subtitle: str = None
    breadcrumbs: Optional[List[Breadcrumb]] = None
    tabs: Optional[List[Tab]] = None
    subsections: Optional[List[Subsection]] = None
    template: str = 'page.html'
    prev: PrevNext = None
    next: PrevNext = None
    steps: List[Step] = None
    published: str = None


class SocialMedia(CustomBaseModel):
    twitter: str = None
    github: str = None


class FooterGroupMore(CustomBaseModel):
    label: str
    href: str


class FooterEntry(CustomBaseModel):
    label: str
    href: str
    icon: str = None
    subtitle: str = None
    accent: str = None


class FooterGroup(CustomBaseModel):
    label: str
    href: str = None
    more: FooterGroupMore = None
    entries: List[FooterEntry] = []


class FooterColumn(CustomBaseModel):
    groups: List[FooterGroup] = None
    fullsize: bool = False


class FooterLinks(CustomBaseModel):
    columns: List[FooterColumn] = []


class Footer(CustomBaseModel):
    social: FooterSocial = None
    links: FooterLinks = None


class SectionSidebarSubEntry(CustomBaseModel):
    label: str
    href: str
    is_active: bool = False


class SectionSidebarEntry(CustomBaseModel):
    label: str
    href: str
    is_active: bool = False
    is_new: bool = False
    entries: List[SectionSidebarSubEntry] = []


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
    section_sidebar: List[SectionSidebarEntry] = None

    def static_path(self, docname, other):
        return static_path(self.static_dirname, docname, other)
