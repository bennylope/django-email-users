==================
Django email users
==================

.. image:: https://secure.travis-ci.org/bennylope/django-email-users.svg?branch=master
    :alt: Build Status
    :target: http://travis-ci.org/bennylope/django-email-users

.. image:: https://pypip.in/v/django-email-users/badge.svg
    :alt: Current PyPI release
    :target: https://pypi.python.org/pypi/django-email-users

.. image:: https://pypip.in/d/django-email-users/badge.svg
    :alt: Download count
    :target: https://pypi.python.org/pypi/django-email-users

For when you want regular Django users but without the usernames.

This is a stock replacement for Django's `auth.User` model that removes the
`username` field in favor of a unique `email` field.
Both the `User` model and the forms enforce lower
cased email addresses to ensure uniqueness without
surprises.

Inspired by the `users` module in pydanny's original `Django cookiecutter
project template <https://github.com/pydanny/cookiecutter-django/>`_ which I
kept using and then editing to support email addresses.

Installing
----------

Install and download with pip::

    pip install django-email-users

Add to your installed apps in your settings.py file::

    INSTALLED_APPS = (
        'users',
    )

Change your project's configured user in your settings.py file::

    AUTH_USER_MODEL = 'users.User'

Profit.

If you are using South with Django prior to Django 1.7, you will need to use
South 1+.
