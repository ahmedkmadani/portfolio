# Generated by Django 4.2 on 2023-04-23 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0021_alter_certificates_certi_logo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certificates",
            name="certi_logo",
            field=models.ImageField(upload_to="cert/"),
        ),
    ]