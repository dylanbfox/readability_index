# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0006_auto_20141015_1543'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='entry',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 15, 17, 9, 9, 175000), auto_now_add=True),
            preserve_default=False,
        ),
    ]
