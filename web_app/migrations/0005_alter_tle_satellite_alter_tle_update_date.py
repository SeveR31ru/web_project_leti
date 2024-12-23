# Generated by Django 4.2.16 on 2024-11-04 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("web_app", "0004_alter_tle_update_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tle",
            name="satellite",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tles",
                to="web_app.satellite",
            ),
        ),
        migrations.AlterField(
            model_name="tle",
            name="update_date",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
