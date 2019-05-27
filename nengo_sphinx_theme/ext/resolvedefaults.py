import inspect
import warnings

from nengo.params import Default, IntParam, iter_params, StringParam


class TestClass:
    """For testing that defaults are properly rendered in docs."""

    int_param = IntParam("int_param", default=1)
    str_param = StringParam("str_param", default="hello")

    def __init__(self, int_param=Default, str_param=Default):
        pass


class DisplayDefault:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "Default<{!r}>".format(self.value)


def resolve_default(cls, arg, value):
    if value is not Default:
        return value
    else:
        for param in (getattr(cls, name) for name in iter_params(cls)):
            if param.name == arg:
                return DisplayDefault(param.default)
        else:
            warnings.warn(
                "Default value for argument {} of {} could not be "
                "resolved.".format(arg, cls)
            )
            return value


def autodoc_defaults(
    app, what, name, obj, options, signature, return_annotation
):
    if what != "class":
        return signature, return_annotation
    spec = inspect.getfullargspec(obj.__init__)
    if spec.defaults is not None:
        defaults = [
            resolve_default(obj, arg, d)
            for arg, d in zip(spec.args[-len(spec.defaults):], spec.defaults)
        ]
    else:
        defaults = None
    return (
        inspect.formatargspec(
            spec.args,
            spec.varargs,
            spec.varkw,
            defaults,
            spec.kwonlyargs,
            spec.kwonlydefaults,
            spec.annotations,
        ),
        return_annotation,
    )


def setup(app):
    app.connect("autodoc-process-signature", autodoc_defaults)
