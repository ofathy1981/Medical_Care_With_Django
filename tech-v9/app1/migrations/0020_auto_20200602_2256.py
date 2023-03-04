# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-06-02 20:56
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_auto_20200602_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medical_script1',
            name='medic1_cost',
            field=models.DecimalField(blank=True, decimal_places=10, default=Decimal('0.000'), max_digits=19, null=True, verbose_name='تكلفة علاج رقم 1'),
        ),
    ]