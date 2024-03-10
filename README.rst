==================
Django email users
==================

For when you want regular Django users but email as usernames.

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

    INSTALLED_APPS = [
        ...
        'users',
    ]

Change your project's configured user in your settings.py file::

    AUTH_USER_MODEL = 'users.User'

Profit.
