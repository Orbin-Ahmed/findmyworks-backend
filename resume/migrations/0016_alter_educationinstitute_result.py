# Generated by Django 4.1.3 on 2023-02-05 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resume", "0015_alter_userskill_skill"),
    ]

    operations = [
        migrations.AlterField(
            model_name="educationinstitute",
            name="result",
            field=models.CharField(default=0, max_length=20),
        ),
    ]