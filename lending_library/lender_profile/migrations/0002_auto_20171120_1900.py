# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-20 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lender_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lenderprofile',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
