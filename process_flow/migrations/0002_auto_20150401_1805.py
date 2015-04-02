# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('process_flow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='document_id',
            field=models.IntegerField(default=1, verbose_name='Document ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='process',
            name='process_id',
            field=models.IntegerField(default=1, verbose_name='Process ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='relationship',
            name='relation',
            field=models.CharField(max_length=64, choices=[('input', 'Input document'), ('output', 'Output document')]),
            preserve_default=True,
        ),
    ]
