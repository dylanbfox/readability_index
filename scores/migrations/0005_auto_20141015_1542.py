# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0004_entry_ignore'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='summary',
            new_name='summary_detail',
        ),
    ]
