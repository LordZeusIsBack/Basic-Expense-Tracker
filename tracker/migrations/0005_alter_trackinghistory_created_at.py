# Generated by Django 5.1.6 on 2025-02-23 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tracker", "0004_alter_trackinghistory_expense_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trackinghistory",
            name="created_at",
            field=models.DateField(auto_now_add=True),
        ),
    ]
