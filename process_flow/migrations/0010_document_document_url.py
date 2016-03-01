# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('process_flow', '0009_auto_20160229_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='document_url',
            field=models.URLField(default=datetime.datetime(2016, 3, 1, 2, 47, 51, 458802, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
