# Generated by Django 4.1.3 on 2023-02-04 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0007_alter_skills_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="skillquizresult",
            name="skill",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="quiz.skills"
            ),
        ),
    ]
