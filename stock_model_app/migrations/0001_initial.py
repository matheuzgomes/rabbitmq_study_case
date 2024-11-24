# Generated by Django 5.1.1 on 2024-09-23 02:53

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StockModel",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100, unique=True)),
                ("stock_name", models.CharField(db_index=True, max_length=100)),
                ("close_price", models.DecimalField(decimal_places=10, max_digits=21)),
                ("change", models.DecimalField(decimal_places=10, max_digits=21)),
                ("volume", models.DecimalField(decimal_places=10, max_digits=21)),
                ("market_cap", models.DecimalField(decimal_places=10, max_digits=21)),
                ("sector", models.CharField(max_length=20)),
                ("type", models.CharField(max_length=10)),
            ],
        ),
    ]