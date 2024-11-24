# Generated by Django 5.1.1 on 2024-09-30 02:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("stock_model_app", "0009_alter_stockmodel_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stockmodel",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 9, 30, 2, 22, 59, 224933, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="stockmodel",
            name="title",
            field=models.CharField(max_length=100),
        ),
    ]