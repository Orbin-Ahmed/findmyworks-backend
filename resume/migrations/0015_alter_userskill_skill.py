# Generated by Django 4.1.3 on 2023-02-04 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0008_alter_skillquizresult_skill"),
        ("resume", "0014_rename_skill_userskill"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userskill",
            name="skill",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="quiz.skills"
            ),
        ),
    ]