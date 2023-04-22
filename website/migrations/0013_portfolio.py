# Generated by Django 4.2 on 2023-04-22 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0012_certificates_codingskill_education_experience_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Portfolio",
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
                ("project_name", models.CharField(max_length=255)),
                ("client_name", models.CharField(max_length=255)),
                ("project_date", models.CharField(max_length=255)),
                ("project_descripiton", models.CharField(max_length=255)),
                ("project_link", models.CharField(max_length=255)),
                ("category", models.CharField(max_length=255)),
                (
                    "project_image",
                    models.ImageField(
                        null=True, upload_to="website/static/project_img"
                    ),
                ),
            ],
        ),
    ]
