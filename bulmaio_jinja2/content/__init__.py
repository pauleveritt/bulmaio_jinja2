navbar_start = [
    dict(css_class='documentation', accent='primary', icon='book',
         label_wide='Documentation', label_narrow='Docs',
         href='/documentation.html'),
    dict(css_class='videos', accent='success', icon='play-circle',
         label_wide='Videos', label_narrow='Videos',
         href='/videos.html'),
    dict(css_class='blog', accent='rss', icon='rss',
         label_wide='Blog', label_narrow='Blog',
         href='/blog.html'),
    dict(css_class='expo', accent='star', icon='star',
         label_wide='Expo', label_narrow='Expo',
         href='/expo.html'),
    dict(css_class='love', accent='danger', icon='heart',
         label_wide='Love', label_narrow='Love',
         href='/love.html'),
    dict(label_wide='More', label_narrow='More',
         href='/more.html',
         submenu=[
             dict(accent='success', icon='rocket', href='/more/start.html',
                  label='Bulma start',
                  description='A tiny npm package to get started',
                  ),
             dict(accent='primary', icon='certificate',
                  href='/more/made_with.html',
                  label='Made with Bulma',
                  description='The official community badge'),
             dict(accent='bootstrap', icon='exchange-alt',
                  href='/more/bootstrap.html',
                  label='Coming from Bootstrap',
                  description='See how Bulma is an alternative to Bootstrap')
         ]),
]


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
