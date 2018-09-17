# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=100, blank=True)),
                ('password', models.CharField(max_length=100, blank=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Credentails',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_photo', models.ImageField(null=True, upload_to=b'driver_images/', blank=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('mobile', models.CharField(max_length=12, null=True, blank=True)),
                ('new_mobile', models.CharField(max_length=12, null=True, blank=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'User - unique',
            },
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=100, blank=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, null=True, blank=True)),
                ('user', models.ForeignKey(to='demo_apis.User', null=True)),
            ],
            options={
                'verbose_name_plural': 'User Tokens',
            },
        ),
        migrations.AddField(
            model_name='credentials',
            name='user',
            field=models.ForeignKey(blank=True, to='demo_apis.User', null=True),
        ),
    ]
