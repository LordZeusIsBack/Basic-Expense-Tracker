# Generated by Django 5.1.6 on 2025-02-21 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tracker", "0002_alter_trackinghistory_amt"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trackinghistory",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
