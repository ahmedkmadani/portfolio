# Generated by Django 4.2 on 2023-04-22 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0009_alter_service_service_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="About",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("introduction", models.CharField(max_length=500)),
                ("title", models.CharField(max_length=250)),
            ],
        ),
    ]
