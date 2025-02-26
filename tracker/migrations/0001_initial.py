# Generated by Django 5.1.6 on 2025-02-21 22:21

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CurrentBalance",
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
                ("cur_bal", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="TrackingHistory",
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
                ("title", models.CharField(max_length=50)),
                (
                    "expense_type",
                    models.CharField(
                        choices=[("Credit", "Credit"), ("Debit", "Debit")],
                        max_length=50,
                    ),
                ),
                (
                    "amt",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(1)]
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Food", "Food"),
                            ("Transport", "Transport"),
                            ("Utilities", "Utilities"),
                            ("Rent", "Rent"),
                            ("Entertainment", "Entertainment"),
                            ("Miscellaneous", "Miscellaneous"),
                        ],
                        max_length=50,
                    ),
                ),
                ("created_at", models.DateTimeField()),
                (
                    "current_balance",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tracker.currentbalance",
                    ),
                ),
            ],
        ),
    ]
