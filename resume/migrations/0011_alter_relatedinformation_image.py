# Generated by Django 4.1.3 on 2023-01-10 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resume", "0010_institute_total_gpa_institute_total_graduates_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="relatedinformation",
            name="image",
            field=models.URLField(blank=True, null=True),
        ),
    ]
