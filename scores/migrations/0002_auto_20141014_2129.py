# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='lpw',
            field=models.DecimalField(default=0.0, max_digits=4, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='raw_score',
            field=models.DecimalField(default=0.0, max_digits=4, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='rounded_score',
            field=models.IntegerField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='wps',
            field=models.DecimalField(default=0.0, max_digits=4, decimal_places=2),
            preserve_default=False,
        ),
    ]
