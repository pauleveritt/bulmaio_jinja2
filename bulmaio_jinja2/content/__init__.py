from yaml import Loader, load


def load_content(pagename):
    with open(f'bulmaio_jinja2/content/{pagename}', 'r') as f:
        return f.read()


def get_pages():
    return {
        'index.html': dict(
            template='homepage.html',
            content=load_content('index.html')
        ),
        'documentation.html': dict(
            template='documentation_homepage.html',
            content=load_content('documentation.html')
        ),
        'documentation_overview.html': dict(
            template='documentation.html',
            content=load_content('documentation_overview.html')
        ),
        'documentation_start.html': dict(
            template='documentation.html',
            content=load_content('documentation_start.html')
        ),
    }


def load_yaml(filename):
    with open(f'bulmaio_jinja2/content/{filename}.yaml', 'r') as f:
        data = load(f, Loader=Loader)
        return data
