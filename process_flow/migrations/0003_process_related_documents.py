# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('process_flow', '0002_auto_20150401_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='related_documents',
            field=models.ManyToManyField(through='process_flow.Relationship', to='process_flow.Document'),
            preserve_default=True,
        ),
    ]
