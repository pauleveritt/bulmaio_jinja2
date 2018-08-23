from pathlib import Path
from typing import List
from typing import Optional

from pydantic import BaseModel
from sphinx.util import relative_uri


class Breadcrumb(BaseModel):
    label: str
    href: str
    is_active: bool = False


class Tab(BaseModel):
    label: str
    href: str
    is_active: bool = False


class Section(BaseModel):
    label: str
    subheading: str
    href: str
    accent: str
    icon: str


class Page(BaseModel):
    docname: str
    title: str = None
    body: str = None
    subtitle: str = None
    breadcrumbs: Optional[List[Breadcrumb]] = None
    tabs: Optional[List[Tab]] = None
    sections: Optional[List[Section]] = None
    template: str = 'page.html'


class Logo(BaseModel):
    img_url: str = None
    img_file: str = None
    alt: str = None


class SocialMedia(BaseModel):
    twitter: str = None
    github: str = None


class NavbarStartEntry(BaseModel):
    css_class: str = None
    accent: str = None
    icon: str = None
    label: str
    label_narrow: str = None
    href: str


class NavbarEndLink(BaseModel):
    color: str
    href: str
    icon: str


class NavbarEndButton(BaseModel):
    accent: str
    href: str
    label: str


class NavbarEnd(BaseModel):
    links: List[NavbarEndLink] = []
    buttons: List[NavbarEndButton] = []


class Navbar(BaseModel):
    start: List[NavbarStartEntry] = []
    end: NavbarEnd = None


class FooterGroupMore(BaseModel):
    label: str
    href: str


class FooterEntry(BaseModel):
    label: str
    href: str
    icon: str = None
    subtitle: str = None
    accent: str = None


class FooterGroup(BaseModel):
    label: str
    href: str = None
    more: FooterGroupMore = None
    entries: List[FooterEntry] = []


class FooterColumn(BaseModel):
    groups: List[FooterGroup] = None
    fullsize: bool = False


class FooterLinks(BaseModel):
    columns: List[FooterColumn] = []


class Footer(BaseModel):
    links: FooterLinks = None


class Site(BaseModel):
    homepage_url: str = '/'
    logo: Logo = None
    title: str = None
    social_media: SocialMedia = None
    copyright: str = 'All Rights Reserved'
    feed_url: str = ''
    favicon: str = None
    is_debug = False
    description: str = None
    navbar: Navbar = None
    footer: Footer = None
    static_dirname: str = '_static/'

    def static_path(self, other):
        full_other = Path(self.static_dirname + other)
        return relative_uri('index', str(full_other))
