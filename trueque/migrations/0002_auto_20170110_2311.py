# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trueque', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='texto',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='titulo',
        ),
    ]
