# Generated by Django 4.1.3 on 2023-02-04 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0007_alter_skills_name"),
        ("resume", "0012_relatedinformationimage"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="skill",
            name="name",
        ),
        migrations.AddField(
            model_name="skill",
            name="skill",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="quiz.skills"
            ),
        ),
    ]
