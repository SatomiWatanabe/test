# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=120)),
                ('time', models.DateTimeField(auto_now=True)),
                ('message', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='', null=True)),
            ],
        ),
    ]
