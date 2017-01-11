# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trueque', '0002_auto_20170110_2311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_date',
            new_name='fecha_creacion',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='published_date',
            new_name='fecha_publicacion',
        ),
    ]
