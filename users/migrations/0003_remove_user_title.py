# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_update_email_groups_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='title',
        ),
    ]
