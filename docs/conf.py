# -*- coding: utf-8 -*-
#
# Automatically generated by nengo-bones, do not edit this file directly

import os

import nengo_sphinx_theme

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "nbsphinx",
    "nengo_sphinx_theme",
    "nengo_sphinx_theme.ext.backoff",
    "nengo_sphinx_theme.ext.redirects",
    "nengo_sphinx_theme.ext.sourcelinks",
    "notfound.extension",
    "numpydoc",
    "nengo_sphinx_theme.ext.resolvedefaults",
    "nengo_sphinx_theme.ext.autoautosummary",
]

# -- sphinx.ext.autodoc
autoclass_content = "both"  # class and __init__ docstrings are concatenated
autodoc_default_options = {"members": None}
autodoc_member_order = "bysource"  # default is alphabetical

# -- sphinx.ext.doctest
doctest_global_setup = """
import nengo_sphinx_theme
"""

# -- sphinx.ext.intersphinx
intersphinx_mapping = {
    "nengo": ("https://www.nengo.ai/nengo/", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "python": ("https://docs.python.org/3", None),
}

# -- sphinx.ext.todo
todo_include_todos = True

# -- nbsphinx
nbsphinx_timeout = -1

# -- notfound.extension
notfound_template = "404.html"
notfound_urls_prefix = "/nengo-sphinx-theme/"

# -- numpydoc config
numpydoc_show_class_members = False

# -- nengo_sphinx_theme.ext.autoautosummary
autoautosummary_change_modules = {
    "nengo_sphinx_theme.ext.renamed_autoautosummary": [
        "nengo_sphinx_theme.ext.autoautosummary.TestClass",
        "nengo_sphinx_theme.ext.autoautosummary.a_test_function",
    ],
}

# -- nengo_sphinx_theme.ext.sourcelinks
sourcelinks_module = "nengo_sphinx_theme"
sourcelinks_url = "https://github.com/nengo/nengo-sphinx-theme"

# -- sphinx
nitpicky = True
exclude_patterns = [
    "_build",
    "**/.ipynb_checkpoints",
    "examples/test-example.ipynb",
]
linkcheck_timeout = 30
source_suffix = ".rst"
source_encoding = "utf-8"
master_doc = "index"
linkcheck_ignore = [r"http://localhost:\d+"]
linkcheck_anchors = True
default_role = "py:obj"
pygments_style = "sphinx"
user_agent = "nengo_sphinx_theme"
autodoc_typehints = "none"

project = "Nengo Sphinx Theme"
authors = "Applied Brain Research"
copyright = "2019-2020 Applied Brain Research"
version = ".".join(nengo_sphinx_theme.__version__.split(".")[:2])  # Short X.Y version
release = nengo_sphinx_theme.__version__  # Full version, with tags

# -- HTML output
templates_path = ["_templates"]
html_static_path = ["_static"]
html_theme = "nengo_sphinx_theme"
html_title = "Nengo Sphinx Theme {0} docs".format(release)
htmlhelp_basename = "Nengo Sphinx Theme"
html_last_updated_fmt = ""  # Default output format (suppressed)
html_show_sphinx = False
html_favicon = os.path.join("_static", "favicon.ico")
html_theme_options = {
    "nengo_logo": "general-full-light.svg",
    "nengo_logo_color": "#a8acaf",
    "tagmanager_id": "GTM-KWCR2HN",
}
html_redirects = [
    ("redirect/to/nested-page.html", "deeply/nested/testing/page.html"),
]
