# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0003_remove_entry_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='ignore',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
