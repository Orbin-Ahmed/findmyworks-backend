# Generated by Django 4.1.3 on 2022-12-28 15:00

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_remove_educationinstitute_name_institute_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionalinstitute',
            name='responsibility',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), blank=True, null=True, size=50, verbose_name='responsibility'),
        ),
    ]