# Generated by Django 4.1.3 on 2022-12-16 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resume", "0005_alter_professionalinstitute_responsibility"),
    ]

    operations = [
        migrations.AddField(
            model_name="relatedinformation",
            name="publications",
            field=models.JSONField(blank=True, null=True),
        ),
    ]