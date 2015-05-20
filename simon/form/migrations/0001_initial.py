# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('job_number', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=0)),
                ('data', models.IntegerField(default=0)),
            ],
        ),
    ]