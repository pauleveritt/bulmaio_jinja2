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
        'documentation_elements_box.html': dict(
            template='documentation.html',
            content=load_content('documentation_elements_box.html')
        ),
    }
