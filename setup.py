#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import publica_pages

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = publica_pages.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-publica-pages',
    version=version,
    description="""Publica Pages for Django""",
    long_description=readme + '\n\n' + history,
    author='Publica IO',
    author_email='gamaliel@commoncode.com.au',
    url='https://github.com/publica-io/django-publica-pages',
    packages=[
        'publica_pages',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-publica-pages',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
