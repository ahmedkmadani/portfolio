# Generated by Django 4.2 on 2023-04-22 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0006_alter_fact_awards_won_alter_fact_coffee_consumed_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Service",
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
                ("service_name", models.CharField(max_length=30)),
                ("service_descriiption", models.CharField(max_length=30)),
                ("service_icon", models.CharField(max_length=30)),
            ],
        ),
    ]