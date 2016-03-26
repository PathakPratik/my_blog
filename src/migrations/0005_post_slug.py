# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0004_auto_20160324_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
