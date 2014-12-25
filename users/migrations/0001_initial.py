# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('first_name', models.CharField(verbose_name='first name', max_length=30, blank=True)),
                ('last_name', models.CharField(verbose_name='last name', max_length=30, blank=True)),
                ('email', models.EmailField(unique=True, verbose_name='email address', max_length=75)),
                ('title', models.CharField(null=True, max_length=100, blank=True)),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status', help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(default=True, verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', to='auth.Group', blank=True, related_name='user_set', related_query_name='user')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', help_text='Specific permissions for this user.', to='auth.Permission', blank=True, related_name='user_set', related_query_name='user')),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
            bases=(models.Model,),
        ),
    ]
