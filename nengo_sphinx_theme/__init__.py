import os
import warnings

from .version import version as __version__

assert __version__

__copyright__ = "2018 Applied Brain Research"
current_dir = os.path.abspath(os.path.dirname(__file__))


def setup(app):
    app.add_html_theme(
        "nengo_sphinx_theme", os.path.join(current_dir, "theme")
    )
    # Add CSS files
    app.add_stylesheet(os.path.join("css", "normalize.css"))
    app.add_stylesheet(os.path.join("css", "bootstrap.css"))
    app.add_stylesheet(os.path.join("css", "mmenu.all.css"))
    app.add_stylesheet(os.path.join("css", "components.css"))
    app.add_stylesheet(os.path.join("css", "nengo.css"))

    # Add JS files
    app.add_javascript(os.path.join("js", "modernizr.js"))
    app.add_javascript(os.path.join("js", "underscore.min.js"))
    app.add_javascript("doctools.js")
    app.add_javascript(os.path.join("js", "searchtools.js"))
    app.add_javascript(os.path.join("js", "webflow.js"))
    app.add_javascript(os.path.join("js", "bootstrap.js"))
    app.add_javascript(os.path.join("js", "mmenu.all.min.js"))
    app.add_javascript(os.path.join("js", "fontawesome.js"))
    app.add_javascript(os.path.join("js", "custom.js"))

    # validate config
    def validate_config(_, config):
        html_logo = getattr(config, "html_logo", "")
        nengo_logo = getattr(config, "html_theme_options", {}).get(
            "nengo_logo", None)

        if html_logo and nengo_logo:
            warnings.warn("'html_logo' and 'nengo_logo' are both set; "
                          "'nengo_logo' will take precedence")
        elif html_logo:
            warnings.warn("Logo set using 'html_logo', consider using "
                          "'nengo_logo' instead")

    app.connect("config-inited", validate_config)
