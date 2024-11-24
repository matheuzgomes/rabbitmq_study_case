from datetime import datetime
from uuid import UUID

from ninja import Schema


class StockPriceSchema(Schema):
    id: UUID
    title: str
    stock_name: str
    close_price: float | None
    change: float | None
    volume: float | None
    market_cap: float | None
    sector: str | None
    type: str | None
    created_at: datetime
