# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0002_auto_20141014_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='author',
        ),
    ]
