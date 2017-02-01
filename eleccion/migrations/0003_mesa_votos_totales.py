# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eleccion', '0002_mesa_partido_resultado'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesa',
            name='votos_totales',
            field=models.IntegerField(default=0),
        ),
    ]
