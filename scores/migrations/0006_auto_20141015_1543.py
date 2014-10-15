# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0005_auto_20141015_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='summary_detail',
            new_name='summary',
        ),
    ]
