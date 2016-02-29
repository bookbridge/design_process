# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('process_flow', '0007_process_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_id',
            field=models.IntegerField(blank=True, verbose_name='Document ID'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='document',
            name='summary',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
