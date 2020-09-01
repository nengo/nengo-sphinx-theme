#!/usr/bin/env python

# Automatically generated by nengo-bones, do not edit this file directly

import io
import os
import runpy

try:
    from setuptools import find_packages, setup
except ImportError:
    raise ImportError(
        "'setuptools' is required but not installed. To install it, "
        "follow the instructions at "
        "https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py"
    )


def read(*filenames, **kwargs):
    encoding = kwargs.get("encoding", "utf-8")
    sep = kwargs.get("sep", "\n")
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


root = os.path.dirname(os.path.realpath(__file__))
version = runpy.run_path(os.path.join(root, "nengo_sphinx_theme", "version.py"))[
    "version"
]

install_req = [
    "sphinx>=3.0.0",
    "sphinx-notfound-page>=0.5.0",
    "backoff>=1.10.0",
]
docs_req = [
    "jupyter",
    "matplotlib",
    "nbsphinx",
    "nengo",
    "numpydoc",
]
optional_req = []
tests_req = []

setup(
    name="nengo-sphinx-theme",
    version=version,
    author="Applied Brain Research",
    author_email="info@appliedbrainresearch.com",
    packages=find_packages(),
    url="https://www.nengo.ai/nengo-sphinx-theme",
    include_package_data=True,
    license="Free for non-commercial use",
    description="Sphinx theme for Nengo project documentation pages",
    long_description=read("README.rst", "CHANGES.rst"),
    zip_safe=False,
    install_requires=install_req,
    extras_require={
        "all": docs_req + optional_req + tests_req,
        "docs": docs_req,
        "optional": optional_req,
        "tests": tests_req,
    },
    python_requires=">=3.5",
    entry_points={
        "sphinx.html_themes": [
            "nengo_sphinx_theme=nengo_sphinx_theme",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Nengo",
        "Intended Audience :: Developers",
        "License :: Free for non-commercial use",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development",
    ],
)
