# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_auto_20160322_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default=2, max_length=45),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
