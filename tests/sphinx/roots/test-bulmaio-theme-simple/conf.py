import inspect
from pathlib import Path

from bulmaio_jinja2.footer.models import Footer
from bulmaio_jinja2.navbar.models import Navbar
from bulmaio_jinja2.sidebar.page.models import PageSidebar
from bulmaio_jinja2.site.models import Site
from bulmaio_jinja2.utils import load_yaml

extensions = [
    'bulmaio_jinja2'
]

html_theme = 'bulmaio_jinja2'
master_doc = 'index'
exclude_patterns = ['_build']

# For test purposes, use the "sample" data for site, navbar, etc.
sample = Path(inspect.getfile(Site)).parents[2] / 'bulmaio_jinja2' / 'sample'
site_yaml = load_yaml('site', base_dir=sample)
site = Site(**site_yaml)
navbar_yaml = load_yaml('navbar', base_dir=sample)
navbar = Navbar(**navbar_yaml)
footer_yaml = load_yaml('footer', base_dir=sample)
footer = Footer(**footer_yaml)
sidebar_yaml = load_yaml('page_sidebar', base_dir=sample)
sidebar = PageSidebar(**sidebar_yaml)

bulmaio_jinja2_site = site
bulmaio_jinja2_navbar = navbar
bulmaio_jinja2_footer = footer
bulmaio_jinja2_sidebar = sidebar

