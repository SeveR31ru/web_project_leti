# Generated by Django 4.2.16 on 2024-11-04 16:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web_app", "0003_rename_image_url_satellite_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tle",
            name="update_date",
            field=models.DateField(auto_now=True),
        ),
    ]
