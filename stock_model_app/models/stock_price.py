from django.db import models

# Create your models here.

class StockModel(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, db_index=True)
    title = models.CharField(max_length=100)
    stock_name = models.CharField(max_length=100, db_index=True)
    close_price = models.DecimalField(default=0.00, decimal_places=24, max_digits=38)
    change = models.DecimalField(default=0.00, decimal_places=24, max_digits=38)
    volume = models.DecimalField(default=0.00, decimal_places=24, max_digits=38)
    market_cap = models.DecimalField(default=0.00, decimal_places=24, max_digits=38)
    sector = models.CharField(max_length=20, null=True)
    type = models.CharField(max_length=10, null=True)
    created_at = models.DateTimeField()

    class Meta:
        db_table = "tb_stock_info"

    def __str__(self) -> str:
        return self.title
