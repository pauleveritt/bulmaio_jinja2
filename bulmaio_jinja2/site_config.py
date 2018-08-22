from typing import List

from pydantic import BaseModel


class Logo(BaseModel):
    img_url: str = None
    img_file: str = None
    alt: str = None


class SocialMedia(BaseModel):
    twitter: str = None
    github: str = None


class NavbarStartEntry(BaseModel):
    css_class: str
    accent: str
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
    links: List[NavbarEndLink]
    buttons: List[NavbarEndButton]


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


class SiteConfig(BaseModel):
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
