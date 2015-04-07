# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('process_flow', '0004_document_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('requirement_number', models.CharField(max_length=32)),
                ('original_requirement', models.TextField(verbose_name='Requirementの原文')),
                ('interpreted_requirement', models.TextField(verbose_name='Requirementの解釈')),
                ('related_documents', models.ManyToManyField(to='process_flow.Document')),
                ('related_process', models.ManyToManyField(to='process_flow.Process')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
