# Generated by Django 4.0.7 on 2022-10-26 14:30

import apps.glue
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_key', apps.glue.FixedCharField(db_column='LOCATION_KEY', max_length=16, primary_key=True, serialize=False)),
                ('description', apps.glue.RtfTextField(blank=True, db_column='DESCRIPTION', null=True)),
                ('spatial_ref', models.CharField(blank=True, db_column='SPATIAL_REF', max_length=40, null=True)),
                ('spatial_ref_system', models.CharField(db_column='SPATIAL_REF_SYSTEM', max_length=4)),
                ('lat', models.FloatField(db_column='LAT')),
                ('long', models.FloatField(db_column='LONG')),
                ('file_code', models.CharField(blank=True, db_column='FILE_CODE', max_length=20, null=True)),
                ('spatial_ref_qualifier', models.CharField(db_column='SPATIAL_REF_QUALIFIER', max_length=20)),
                ('approach', apps.glue.RtfTextField(blank=True, db_column='APPROACH', null=True)),
                ('restriction', apps.glue.RtfTextField(blank=True, db_column='RESTRICTION', null=True)),
                ('entered_by', apps.glue.FixedCharField(db_column='ENTERED_BY', max_length=16)),
                ('entry_date', models.DateTimeField(db_column='ENTRY_DATE')),
                ('changed_by', apps.glue.FixedCharField(blank=True, db_column='CHANGED_BY', max_length=16, null=True)),
                ('changed_date', models.DateTimeField(blank=True, db_column='CHANGED_DATE', null=True)),
                ('system_supplied_data', models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')),
                ('custodian', apps.glue.FixedCharField(blank=True, db_column='CUSTODIAN', max_length=8, null=True)),
            ],
            options={
                'db_table': 'LOCATION',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LocationDesignation',
            fields=[
                ('designation_key', apps.glue.FixedCharField(db_column='DESIGNATION_KEY', max_length=16, primary_key=True, serialize=False)),
                ('ref_code', models.CharField(blank=True, db_column='REF_CODE', max_length=20, null=True)),
                ('date_from', models.DateTimeField(blank=True, db_column='DATE_FROM', null=True)),
                ('date_to', models.DateTimeField(blank=True, db_column='DATE_TO', null=True)),
                ('comment', models.TextField(blank=True, db_column='COMMENT', null=True)),
                ('entered_by', apps.glue.FixedCharField(db_column='ENTERED_BY', max_length=16)),
                ('entry_date', models.DateTimeField(db_column='ENTRY_DATE')),
                ('changed_by', apps.glue.FixedCharField(blank=True, db_column='CHANGED_BY', max_length=16, null=True)),
                ('changed_date', models.DateTimeField(blank=True, db_column='CHANGED_DATE', null=True)),
                ('system_supplied_data', models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')),
                ('custodian', apps.glue.FixedCharField(blank=True, db_column='CUSTODIAN', max_length=8, null=True)),
            ],
            options={
                'db_table': 'LOCATION_DESIGNATION',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LocationName',
            fields=[
                ('location_name_key', apps.glue.FixedCharField(db_column='LOCATION_NAME_KEY', max_length=16, primary_key=True, serialize=False)),
                ('item_name', models.CharField(db_column='ITEM_NAME', max_length=100)),
                ('preferred', models.BooleanField(db_column='PREFERRED')),
                ('entered_by', apps.glue.FixedCharField(db_column='ENTERED_BY', max_length=16)),
                ('entry_date', models.DateTimeField(db_column='ENTRY_DATE')),
                ('changed_by', apps.glue.FixedCharField(blank=True, db_column='CHANGED_BY', max_length=16, null=True)),
                ('changed_date', models.DateTimeField(blank=True, db_column='CHANGED_DATE', null=True)),
                ('custodian', apps.glue.FixedCharField(blank=True, db_column='CUSTODIAN', max_length=8, null=True)),
            ],
            options={
                'db_table': 'LOCATION_NAME',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LocationType',
            fields=[
                ('location_type_key', apps.glue.FixedCharField(db_column='LOCATION_TYPE_KEY', max_length=16, primary_key=True, serialize=False)),
                ('short_name', models.CharField(db_column='SHORT_NAME', max_length=20)),
                ('long_name', models.CharField(blank=True, db_column='LONG_NAME', max_length=100, null=True)),
                ('description', models.CharField(blank=True, db_column='DESCRIPTION', max_length=200, null=True)),
                ('authority', models.CharField(blank=True, db_column='AUTHORITY', max_length=100, null=True)),
                ('entered_by', apps.glue.FixedCharField(db_column='ENTERED_BY', max_length=16)),
                ('entry_date', models.DateTimeField(db_column='ENTRY_DATE')),
                ('changed_by', apps.glue.FixedCharField(blank=True, db_column='CHANGED_BY', max_length=16, null=True)),
                ('changed_date', models.DateTimeField(blank=True, db_column='CHANGED_DATE', null=True)),
                ('system_supplied_data', models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')),
                ('custodian', apps.glue.FixedCharField(blank=True, db_column='CUSTODIAN', max_length=8, null=True)),
            ],
            options={
                'db_table': 'LOCATION_TYPE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SiteStatus',
            fields=[
                ('site_status_key', apps.glue.FixedCharField(db_column='SITE_STATUS_KEY', max_length=16, primary_key=True, serialize=False)),
                ('short_name', models.CharField(db_column='SHORT_NAME', max_length=40)),
                ('long_name', models.CharField(blank=True, db_column='LONG_NAME', max_length=100, null=True)),
                ('description', models.TextField(blank=True, db_column='DESCRIPTION', null=True)),
                ('entered_by', apps.glue.FixedCharField(db_column='ENTERED_BY', max_length=16)),
                ('entry_date', models.DateTimeField(db_column='ENTRY_DATE')),
                ('changed_by', apps.glue.FixedCharField(blank=True, db_column='CHANGED_BY', max_length=16, null=True)),
                ('changed_date', models.DateTimeField(blank=True, db_column='CHANGED_DATE', null=True)),
                ('system_supplied_data', models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')),
                ('custodian', apps.glue.FixedCharField(blank=True, db_column='CUSTODIAN', max_length=8, null=True)),
            ],
            options={
                'db_table': 'SITE_STATUS',
                'managed': False,
            },
        ),
    ]
