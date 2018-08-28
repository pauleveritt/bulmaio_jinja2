from bulmaio_jinja2.base_model import CustomBaseModel


class FooterSocialProjectAuthor(CustomBaseModel):
    name: str
    website: str
    twitter: str = None


class FooterSocialLicense(CustomBaseModel):
    name: str
    href: str


class FooterSocialProjectGitHub(CustomBaseModel):
    user: str
    repo: str


class FooterSocialProject(CustomBaseModel):
    """ A project the website might be associated with """
    title: str
    author: FooterSocialProjectAuthor
    license: FooterSocialLicense
    github: FooterSocialProjectGitHub = None


class FooterSocialSite(CustomBaseModel):
    """ This website content """
    title: str
    license: FooterSocialLicense
    author: FooterSocialProjectAuthor


class FooterShareTwitter(CustomBaseModel):
    url: str
    related: str


class FooterShare(CustomBaseModel):
    twitter: FooterShareTwitter


class FooterSocial(CustomBaseModel):
    project: FooterSocialProject
    site: FooterSocialSite
    share: FooterShare
