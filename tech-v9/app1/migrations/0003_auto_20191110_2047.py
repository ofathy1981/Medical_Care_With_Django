# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-11-10 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_doctor_clinic_hospital_laboratory_mdeical_transform_medical_script_midicine_retired_pationt_scan_cen'),
    ]

    operations = [
        migrations.AddField(
            model_name='mdeical_transform',
            name='rcvd_service',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='نوع الرعاية الطبية '),
        ),
        migrations.AlterField(
            model_name='mdeical_transform',
            name='followed_clinic',
            field=models.CharField(choices=[('جاردن سيتى', 'جاردن سيتى'), ('الفوالة', 'الفوالة'), ('المهندسيين', 'المهندسيين')], max_length=120, verbose_name=' '),
        ),
        migrations.AlterField(
            model_name='mdeical_transform',
            name='medical_number',
            field=models.CharField(max_length=120, verbose_name='الرقم الطبى '),
        ),
        migrations.AlterField(
            model_name='mdeical_transform',
            name='to_clinic',
            field=models.ForeignKey(choices=[('جاردن سيتى', 'جاردن سيتى'), ('الفوالة', 'الفوالة'), ('المهندسيين', 'المهندسيين')], max_length=120, on_delete=django.db.models.deletion.CASCADE, to='app1.doctor_clinic', verbose_name=' اختر العيادة خارجية'),
        ),
        migrations.AlterField(
            model_name='mdeical_transform',
            name='to_hospital',
            field=models.ForeignKey(max_length=120, on_delete=django.db.models.deletion.CASCADE, to='app1.hospital', verbose_name=' اختر المستشفى'),
        ),
        migrations.AlterField(
            model_name='mdeical_transform',
            name='to_lab',
            field=models.ForeignKey(choices=[('جاردن سيتى', 'جاردن سيتى'), ('الفوالة', 'الفوالة'), ('المهندسيين', 'المهندسيين')], max_length=120, on_delete=django.db.models.deletion.CASCADE, to='app1.laboratory', verbose_name='اختر المعمل او مركز الاشعة  '),
        ),
        migrations.AlterField(
            model_name='medical_script',
            name='medic1_name',
            field=models.CharField(max_length=120, verbose_name='علاج 1'),
        ),
        migrations.AlterField(
            model_name='medical_script',
            name='medic2_name',
            field=models.CharField(max_length=120, verbose_name='2 علاج '),
        ),
        migrations.AlterField(
            model_name='medical_script',
            name='medic3_name',
            field=models.CharField(max_length=120, verbose_name='3 علاج '),
        ),
        migrations.AlterField(
            model_name='medical_script',
            name='medic4_name',
            field=models.CharField(max_length=120, verbose_name='4  علاج'),
        ),
        migrations.AlterField(
            model_name='medical_script',
            name='medic5_name',
            field=models.CharField(max_length=120, verbose_name='علاج 5  '),
        ),
        migrations.AlterField(
            model_name='medical_script',
            name='medic6_name',
            field=models.CharField(max_length=120, verbose_name='6 علاج '),
        ),
        migrations.AlterField(
            model_name='medical_script',
            name='medic7_name',
            field=models.CharField(max_length=120, verbose_name='علاج 7  '),
        ),
        migrations.AlterField(
            model_name='medical_script',
            name='medical_number',
            field=models.CharField(max_length=120, verbose_name='الرقم الطبى '),
        ),
    ]
