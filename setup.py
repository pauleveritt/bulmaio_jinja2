from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bulmaio_jinja2',
    version='0.0.1',
    description='Jinja2 templating for the bulma.io site structure and styling',
    long_description=long_description,
    url='https://github.com/pauleveritt/bulmaio_jinja2',
    author='Paul Everitt',
    author_email='pauleveritt@me.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.y',
    ],
    keywords='bulma jinja2',
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=[
        'jinja2',
    ],
    include_package_data=True
)
