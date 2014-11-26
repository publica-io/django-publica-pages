# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='page',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='page',
            name='featured',
        ),
        migrations.RemoveField(
            model_name='page',
            name='modified_at',
        ),
        migrations.RemoveField(
            model_name='page',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='page',
            name='published_at',
        ),
    ]
