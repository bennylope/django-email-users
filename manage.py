#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Management command entry point for working with migrations
"""

import sys
import django
from django.conf import settings

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "users",
]

settings.configure(
    DEBUG=True,
    USE_TZ=True,
    USE_I18N=True,
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
        }
    },
    AUTH_USER_MODEL='users.User',
    MIDDLEWARE_CLASSES=(),
    SITE_ID=1,
    INSTALLED_APPS=INSTALLED_APPS,
)

django.setup()


if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
