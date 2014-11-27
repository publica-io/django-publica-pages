# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20141126_2213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': 'Content Page', 'verbose_name_plural': 'Content Pages with Page Content Views'},
        ),
        migrations.AlterField(
            model_name='page',
            name='preview_template',
            field=models.ForeignKey(related_name='pages_page_preview_templates', blank=True, to='templates.Template', help_text=b'Optionally choose a Listing Template that will be used in List Views', null=True, verbose_name=b'Listing/Preview Template'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='template',
            field=models.ForeignKey(related_name='pages_page_templates', blank=True, to='templates.Template', help_text=b'Choose a template to render this content', null=True),
            preserve_default=True,
        ),
    ]
