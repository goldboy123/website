# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_catalog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='catalog',
            field=models.ForeignKey(default=0, to='blog.Catalog'),
            preserve_default=False,
        ),
    ]
