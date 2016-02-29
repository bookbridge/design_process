# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('process_flow', '0005_requirement'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='summary',
            field=models.TextField(default=datetime.datetime(2016, 2, 29, 14, 18, 19, 127516, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
