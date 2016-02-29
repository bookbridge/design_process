# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('process_flow', '0008_auto_20160229_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_id',
            field=models.IntegerField(verbose_name='Document ID'),
            preserve_default=True,
        ),
    ]
