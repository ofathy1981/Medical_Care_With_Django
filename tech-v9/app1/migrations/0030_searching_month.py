# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-06-09 23:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0029_auto_20200609_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='searching',
            name='month',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], max_length=120, null=True, verbose_name=' اختر  الشهر'),
        ),
    ]
