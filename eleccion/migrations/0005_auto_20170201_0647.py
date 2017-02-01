# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eleccion', '0004_auto_20170201_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipo',
            field=models.CharField(max_length=3, choices=[('GES', 'Usuario gestor'), ('SUP', 'Usuario supervisor')]),
        ),
    ]
