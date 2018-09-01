import os
from pathlib import Path

from bulmaio_jinja2.footer.models import Footer
from bulmaio_jinja2.navbar.models import Navbar
from bulmaio_jinja2.sample import Pages
from bulmaio_jinja2.sidebar.page.models import PageSidebar
from bulmaio_jinja2.sidebar.section.models import SectionSidebar
from bulmaio_jinja2.site.models import Site
from bulmaio_jinja2.tutorial.models import TutorialSidebar
from bulmaio_jinja2.utils import load_yaml
from flask import Flask, render_template, send_from_directory, make_response
from jinja2 import ChoiceLoader, PackageLoader

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_loader = ChoiceLoader([
    PackageLoader('bulmaio_jinja2', 'templates'),
    PackageLoader('bulmaio_jinja2', '.'),
])

cwd = Path(__file__).parents[0] / 'sample'


@app.route('/bulmaio_jinja2.map')
def sourcemaps():
    # Likely a problem with Parcel encoding an absolute path in the .js
    # to point at the .map
    headers = {}
    with open('bulmaio_jinja2/static/bulmaio_jinja2.map', 'r') as f:
        body = f.read()
    return make_response((body, headers))


@app.route('/favicon.ico')
@app.route('/static/favicons/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static', 'favicons'),
        'bulma-logo.png',
        mimetype='image/vnd.microsoft.icon')


@app.route('/', defaults={'pagename': 'index.html'})
@app.route('/<pagename>')
@app.route('/<foldername>/<pagename>')
def page_view(pagename, foldername=None):
    # If we are in a folder, join its name with the pagename
    if foldername:
        pagename = foldername + '/' + pagename

    # Make a Site with a Footer
    site = Site(**load_yaml('site', base_dir=cwd))
    site.static_dirname = 'static/'  # Don't use Sphinx name

    # Get some globals. Jam them in here so that livereload will get them,
    # slows down requests for development, but that's ok.
    pages = Pages()
    pages.load_pages()

    # Get this page
    page = pages.get(pagename)

    # Make a navbar with site-specific and page-specific data
    navbar = Navbar(**load_yaml('navbar', base_dir=cwd))
    navbar.update(site, page)

    # Make a footer
    footer = Footer(**load_yaml('footer', base_dir=cwd))

    # Make a sidebar...it's either a section_sidebar or per-resource
    sidebar = None
    if page.template == 'section.html':
        section_sidebar = load_yaml('section_sidebar', base_dir=cwd)
        sidebar = SectionSidebar(**section_sidebar)
    elif page.template == 'page.html':
        page_sidebar = load_yaml('page_sidebar', base_dir=cwd)
        sidebar = PageSidebar(**page_sidebar)
    elif page.template in ['tutorial.html', 'tutorialpage.html']:
        tutorial_sidebar = load_yaml('tutorial_sidebar', base_dir=cwd)
        sidebar = TutorialSidebar(**tutorial_sidebar)

    try:
        active_category = [
            category
            for category in sidebar.entries
            if category.href[1:-6] in page.docname
        ]
        if active_category:
            active_category[0].is_active = True
    except AttributeError:
        pass

    # Make a context
    context = dict(
        site=site,
        page=page,
        navbar=navbar,
        sidebar=sidebar,
        footer=footer
    )

    return render_template(page.template, **context)
