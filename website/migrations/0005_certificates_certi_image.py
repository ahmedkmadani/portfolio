# Generated by Django 3.2.18 on 2023-04-25 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_client_client_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificates',
            name='certi_image',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
