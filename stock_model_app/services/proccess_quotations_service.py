import json
import logging
from datetime import UTC, datetime
from uuid import uuid4

from ..models import StockModel
from ..schemas import StockPriceSchema
from ..utils import (
    CheckDecimalFieldNullability,
)


class ProcessQuotationsService:

    def execute(self, ch, method, properties, body) -> None:

        formatted_body = body.decode().replace("'", '"').replace("None", "null")

        data_dict = json.loads(formatted_body)

        quotation_data = StockPriceSchema(
                id=uuid4(),
                title=data_dict["stock"],
                stock_name=data_dict["name"],
                close_price=CheckDecimalFieldNullability.execute(data_dict["close"]),
                change=CheckDecimalFieldNullability.execute(data_dict["change"]),
                volume=CheckDecimalFieldNullability.execute(data_dict["volume"]),
                market_cap=CheckDecimalFieldNullability.execute(data_dict["market_cap"]),
                sector=data_dict["sector"],
                type=data_dict["type"],
                created_at=datetime.now(UTC),
            )

        StockModel.objects.create(**quotation_data.dict())

        logging.info(f"inserted quotation {quotation_data}")