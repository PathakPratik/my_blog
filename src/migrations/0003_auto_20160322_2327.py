# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_auto_20160110_1453'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post1',
            new_name='Post',
        ),
    ]
