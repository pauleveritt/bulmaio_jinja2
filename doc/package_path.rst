=============
Package Paths
=============

In Jinja2-based systems such as Sphinx, you often want to refer to a
static asset in some HTML tag, such as ``<script>``, ``<link>``, or
``<img>``.

Sphinx provides a ``pathto`` helper, but it doesn't help find
assets in packages. Instead, those packages have to inject directories
into Sphinx's ``pathto`` list of directories and let Sphinx wander around
looking.

Python 3.7 has a way to refer to a file in a package, with a backport to
Python 3.6. ``bulmaio_jinja2`` provides a ``pkgpathto`` function which
uses this to locate its assets. It also provides a helper to inject
this function into the Jinja2 context for Sphinx.