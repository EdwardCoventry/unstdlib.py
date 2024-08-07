#!/usr/bin/env python

from distutils.core import setup

try:
    import setuptools
except ImportError:
    pass # No 'develop' command, oh well.

version = '0.1'

setup(name='unstdlib',
    version=version,
    description='Unstandard Python library of useful and highly-reusable functions',
    author='Andrey Petrov',
    author_email='andrey.petrov@shazow.net',
    url='https://github.com/shazow/unstdlib.py',
    packages=['unstdlib', 'unstdlib.standard'],
    long_description="""
    Have you ever written code that you used in more than one project? Me too.

    ``unstdlib`` is a compilation of highly-reusable code for Python.
    """.strip(),
    license="MIT",
    platforms=["any"],
)
