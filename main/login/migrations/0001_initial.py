# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('hometown', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(upload_to='')),
            ],
        ),
    ]