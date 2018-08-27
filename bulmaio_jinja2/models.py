from pathlib import Path
from typing import List
from typing import Optional

from pydantic import BaseModel
from sphinx.util import relative_uri


class CustomBaseModel(BaseModel):
    class Config:
        ignore_extra = False


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


class Logo(CustomBaseModel):
    img_url: str = None
    img_file: str = None
    alt: str = None


class SocialMedia(CustomBaseModel):
    twitter: str = None
    github: str = None


class NavbarStartSubEntry(CustomBaseModel):
    css_class: str = None
    accent: str = None
    icon: str = None
    label: str
    description: str = None
    label_narrow: str = None
    href: str


class NavbarStartEntry(CustomBaseModel):
    css_class: str = None
    accent: str = None
    icon: str = None
    label: str
    label_narrow: str = None
    href: str
    submenu: List[NavbarStartSubEntry] = None


class NavbarEndLink(CustomBaseModel):
    color: str
    href: str
    icon: str


class NavbarEndButton(CustomBaseModel):
    accent: str
    href: str
    label: str


class NavbarEnd(CustomBaseModel):
    links: List[NavbarEndLink] = []
    buttons: List[NavbarEndButton] = []


class Navbar(CustomBaseModel):
    start: List[NavbarStartEntry] = []
    end: NavbarEnd = None


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
    links: FooterLinks = None


class SidebarSubEntry(CustomBaseModel):
    label: str
    href: str
    is_active: bool = False


class SidebarEntry(CustomBaseModel):
    label: str
    is_active: bool = False
    is_new: bool = False
    entries: List[SidebarSubEntry] = []


class Site(CustomBaseModel):
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
    sidebar: List[SidebarEntry] = None

    def static_path(self, docname, other):
        full_other = Path(self.static_dirname, other)
        target = relative_uri(docname, str(full_other))
        return target
