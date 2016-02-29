# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('process_flow', '0006_document_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='summary',
            field=models.TextField(default=datetime.datetime(2016, 2, 29, 14, 33, 0, 158789, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
