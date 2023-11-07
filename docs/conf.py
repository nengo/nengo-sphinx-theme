# -*- coding: utf-8 -*-
#
# Automatically generated by nengo-bones, do not edit this file directly

import pathlib

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
linkcheck_ignore = linkcheck_ignore + [r"redirect/to/.*.html"]

project = "Nengo Sphinx Theme"
authors = "Applied Brain Research"
copyright = "2019-2023 Applied Brain Research"
version = ".".join(nengo_sphinx_theme.__version__.split(".")[:2])  # Short X.Y version
release = nengo_sphinx_theme.__version__  # Full version, with tags

# -- HTML output
templates_path = ["_templates"]
html_static_path = ["_static"]
html_theme = "nengo_sphinx_theme"
html_title = f"Nengo Sphinx Theme {release} docs"
htmlhelp_basename = "Nengo Sphinx Theme"
html_last_updated_fmt = ""  # Default output format (suppressed)
html_show_sphinx = False
html_favicon = str(pathlib.Path("_static", "favicon.ico"))
html_theme_options = {
    "nengo_logo": "general-full-light.svg",
    "nengo_logo_color": "#a8acaf",
    "analytics": """
        <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-GT8XEDLTMJ"></script>
        <script>
         window.dataLayer = window.dataLayer || [];
         function gtag(){dataLayer.push(arguments);}
         gtag('js', new Date());
         gtag('config', 'G-GT8XEDLTMJ');
        </script>
        <!-- End Google tag (gtag.js) -->
        <!-- Matomo -->
        <script>
         var _paq = window._paq = window._paq || [];
         _paq.push(["setDocumentTitle", document.domain + "/" + document.title]);
         _paq.push(["setCookieDomain", "*.appliedbrainresearch.com"]);
         _paq.push(["setDomains", ["*.appliedbrainresearch.com","*.edge.nengo.ai","*.forum.nengo.ai","*.nengo.ai"]]);
         _paq.push(["enableCrossDomainLinking"]);
         _paq.push(["setDoNotTrack", true]);
         _paq.push(['trackPageView']);
         _paq.push(['enableLinkTracking']);
         (function() {
           var u="https://appliedbrainresearch.matomo.cloud/";
           _paq.push(['setTrackerUrl', u+'matomo.php']);
           _paq.push(['setSiteId', '3']);
           var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
           g.async=true; g.src='//cdn.matomo.cloud/appliedbrainresearch.matomo.cloud/matomo.js'; s.parentNode.insertBefore(g,s);
         })();
        </script>
        <!-- End Matomo Code -->
    """,
}
html_redirects = [
    ("redirect/to/nested-page.html", "deeply/nested/testing/page.html"),
    ("redirect/to/external.html", "https://www.nengo.ai/"),
]
