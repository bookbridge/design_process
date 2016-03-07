# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Entry',
            new_name='FAQ',
        ),
        migrations.AlterModelOptions(
            name='faq',
            options={'ordering': ['-pub_date']},
        ),
    ]
