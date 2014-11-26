# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import entropy.mixins


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('templates', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(default=b'', blank=True)),
                ('title', models.CharField(max_length=255)),
                ('short_title', models.CharField(max_length=255, blank=True)),
                ('slug', models.SlugField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('enabled', models.BooleanField(default=False, db_index=True)),
                ('featured', models.BooleanField(default=False)),
                ('published_at', models.DateField(null=True)),
                ('created_by', models.ForeignKey(related_name='pages_page_created_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='pages_page_modified_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('preview_template', models.ForeignKey(related_name='pages_page_preview_templates', blank=True, to='templates.Template', null=True)),
                ('template', models.ForeignKey(related_name='pages_page_templates', blank=True, to='templates.Template', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(entropy.mixins.BaseSlugMixin, models.Model),
        ),
    ]
