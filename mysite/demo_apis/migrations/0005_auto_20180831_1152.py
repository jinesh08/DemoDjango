# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_apis', '0004_auto_20180831_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_photo',
            field=models.ImageField(null=True, upload_to=b'user_images/', blank=True),
        ),
    ]
