# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trueque', '0003_auto_20170110_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=200)),
                ('texto', models.TextField()),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('aceptado', models.BooleanField(default=False)),
                ('post', models.ForeignKey(to='trueque.Post', related_name='comments')),
            ],
        ),
    ]
