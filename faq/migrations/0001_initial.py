# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('pub_date', models.DateTimeField(verbose_name='entry published')),
                ('contents', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
