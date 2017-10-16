# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 16:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20171013_0922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jurisdiction',
            old_name='jurisdictionAbbrv',
            new_name='abbrv',
        ),
        migrations.RenameField(
            model_name='jurisdiction',
            old_name='jurisdictionName',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='volocation',
            old_name='AddlDeliveryInfo',
            new_name='addlDeliveryInfo',
        ),
        migrations.RenameField(
            model_name='volocation',
            old_name='Addressee',
            new_name='addressee',
        ),
        migrations.RemoveField(
            model_name='voclaimtype',
            name='claimSchemaDefinition',
        ),
        migrations.AddField(
            model_name='user',
            name='effectiveDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='user',
            name='endDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userrole',
            name='effectiveDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='userrole',
            name='endDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]