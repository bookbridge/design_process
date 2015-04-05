# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('process_flow', '0003_process_related_documents'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='description',
            field=models.TextField(default=datetime.datetime(2015, 4, 5, 16, 44, 10, 989334, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
