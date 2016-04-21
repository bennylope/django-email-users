#!/usr/bin/env python
# -*- coding: utf-8 -*-

import users

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = users.__version__

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-email-users',
    version=version,
    description="""Stock user app but without usernames""",
    long_description=readme + '\n\n' + history,
    author='Ben Lopatin',
    author_email='ben@benlopatin.com',
    url='https://github.com/bennylope/django-email-users',
    packages=[
        'users',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-email-users',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
