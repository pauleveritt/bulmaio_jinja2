from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bulmaio_jinja2',
    version='0.0.1',
    description='Jinja2 templating for the bulma.io site structure and '
                'styling',
    long_description=long_description,
    url='https://github.com/pauleveritt/bulmaio_jinja2',
    author='Paul Everitt',
    author_email='pauleveritt@me.com',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='bulma jinja2',
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=[
        'jinja2',
        'pydantic',
        'importlib_resources;python_version<"3.4"',
    ],
    include_package_data=True,
    entry_points={
        'sphinx.html_themes': [
            'bulmaio_jinja2 = bulmaio_jinja2',
        ]
    },
)
