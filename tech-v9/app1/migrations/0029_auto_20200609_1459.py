# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-06-09 12:59
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0028_monthly_medical_script1_paper_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='mdeical_transform1',
            name='paper_code',
            field=models.CharField(default=uuid.uuid4, max_length=120),
        ),
        migrations.AddField(
            model_name='mdeical_transform2',
            name='cost_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mdeical_transform2',
            name='paper_code',
            field=models.CharField(default=uuid.uuid4, max_length=120),
        ),
        migrations.AddField(
            model_name='mdeical_transform2',
            name='trans_to',
            field=models.CharField(blank=True, choices=[('عيادة', 'عيادة'), ('معمل', 'معمل'), ('مستشفى', 'مستشفى')], max_length=120, null=True, verbose_name='التحويل الـى'),
        ),
        migrations.AddField(
            model_name='mdeical_transform2',
            name='transform_cost',
            field=models.DecimalField(blank=True, decimal_places=3, default=Decimal('0.000'), max_digits=19, null=True, verbose_name='تكلفة التحويل الطبى'),
        ),
        migrations.AddField(
            model_name='mdeical_transform3',
            name='paper_code',
            field=models.CharField(default=uuid.uuid4, max_length=120),
        ),
        migrations.AddField(
            model_name='mdeical_transform3',
            name='trans_to',
            field=models.CharField(blank=True, choices=[('عيادة', 'عيادة'), ('معمل', 'معمل'), ('مستشفى', 'مستشفى')], max_length=120, null=True, verbose_name='التحويل الـى'),
        ),
        migrations.AddField(
            model_name='mdeical_transform3',
            name='transform_cost',
            field=models.DecimalField(blank=True, decimal_places=3, default=Decimal('0.000'), max_digits=19, null=True, verbose_name='تكلفة التحويل الطبى'),
        ),
        migrations.AddField(
            model_name='medical_script1',
            name='paper_code',
            field=models.CharField(default=uuid.uuid4, max_length=120),
        ),
        migrations.AddField(
            model_name='medical_script2',
            name='paper_code',
            field=models.CharField(default=uuid.uuid4, max_length=120),
        ),
        migrations.AddField(
            model_name='medical_script2',
            name='total_medic_cost',
            field=models.DecimalField(blank=True, decimal_places=3, default=Decimal('0.000'), max_digits=19, null=True, verbose_name='إجمالى التكاليف   '),
        ),
        migrations.AddField(
            model_name='medical_script2',
            name='updated',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='medical_script3',
            name='paper_code',
            field=models.CharField(default=uuid.uuid4, max_length=120),
        ),
        migrations.AddField(
            model_name='medical_script3',
            name='total_medic_cost',
            field=models.DecimalField(blank=True, decimal_places=3, default=Decimal('0.000'), max_digits=19, null=True, verbose_name='إجمالى التكاليف   '),
        ),
        migrations.AddField(
            model_name='monthly_medical_script2',
            name='Added',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='monthly_medical_script2',
            name='master',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='monthly_medical_script2',
            name='paper_code',
            field=models.CharField(default=uuid.uuid4, max_length=120),
        ),
        migrations.AddField(
            model_name='monthly_medical_script2',
            name='total_cost',
            field=models.DecimalField(blank=True, decimal_places=3, default=Decimal('0.000'), max_digits=19, null=True, verbose_name='تكلفة علاج رقم 20'),
        ),
        migrations.AddField(
            model_name='monthly_medical_script3',
            name='Added',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='monthly_medical_script3',
            name='master',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='monthly_medical_script3',
            name='paper_code',
            field=models.CharField(default=uuid.uuid4, max_length=120),
        ),
        migrations.AddField(
            model_name='monthly_medical_script3',
            name='total_cost',
            field=models.DecimalField(blank=True, decimal_places=3, default=Decimal('0.000'), max_digits=19, null=True, verbose_name='تكلفة علاج رقم 20'),
        ),
        migrations.AlterField(
            model_name='mdeical_transform2',
            name='auth_doc',
            field=models.CharField(choices=[('محمد', 'محمد'), ('', ''), ('', ''), ('', ''), ('', '')], max_length=120, verbose_name='طبيب العيادة '),
        ),
    ]
