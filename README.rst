==============
bulmaio_jinja2
==============

Jinja2 templating for the bulma.io site structure and styling

Bulma is a modern CSS framework and bulma.io is a nicely-structured website.
The bulmaio package extracts the markup, SASS, etc. into a standalone
package.

This package then makes Jinja2 templates, somewhat like components,
which can then be used in a Flask site, Sphinx project, etc. This package
also includes a Sphinx theme.

The primary deliverables for the project are:

- Wheels containing the CSS/JS/images from bulmaio (which isn't
  Python-specific)

- Jinja2 helpers that can resolve package-based paths based on the
  Python 3.7 importlib package (available as a backport to 3.6)

- "Snippets" of some kind (e.g. macros) that make it easy to get Bulma
  and bulma.io structures in a reusable, data-oriented, "I don't want to
  think about it" kind of way

- Optional pydantic models that validate the inputs to those macros

- Improved DX in this package using a Flask dev server and livereload

Install
=======

.. code-block:: bash

    $ pip install bulmaio_jinja2

Python Development
==================

- Clone

- Make a virtual env

- pip install -r requirements.txt

You can also run the livereload Flask server:

.. code-block:: bash

  $ python -m bulmaio_jinja2.livereload

This launches a Flask app with a ``/<pagename>`` route that does the
following:

- Uses dummy content in the ``content`` directory

- Site content is mimicked in ``site.yaml``

- Individual pages are mimicked in ``pages.yaml`` with corresponding
  ``.html`` files

- The ``pagename`` is looked up from pages

- A Jinja2 ``context`` is assembled that includes the ``site``,
  the ``navbar``, and the ``page``

- The template assigned in the ``page`` is rendered with the context

- Whenever anything in the ``bulmaio_jinja2`` directory changes,
  the browser reloads

Web Development
===============

This use SASS, JS minification, etc.

- npm install

- npm start (to run development server with live building using Parcel)

- npm build

Test
====

- pytest tests/unit

- pytest tests/integration

Docs
====

- cd doc

- make html

