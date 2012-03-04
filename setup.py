#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = "pinax-cms-project",
    version = "0.1",
    packages = ['pinax.projects.cms_project'],
    author = "Dmitry Falk",
    author_email = "dfalk5@gmail.com",
    description = "Pinax starter project for Django-CMS",
    url = "https://github.com/dfalk/pinax-cms-project",
    install_requires=['pinax'],
)
