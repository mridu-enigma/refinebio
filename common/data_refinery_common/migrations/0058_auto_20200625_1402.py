# Generated by Django 2.2.13 on 2020-06-25 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data_refinery_common", "0057_fix_platform_accessions_spaces"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dataset",
            name="email_address",
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
    ]