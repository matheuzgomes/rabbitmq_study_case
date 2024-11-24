import logging
from dataclasses import dataclass

from ..connector.interface import IStockDataConnector
from ..infrastructure import MessagingClient
from ..utils import (
    GenericNotFoundException,
)


@dataclass
class GetAllStocksService:
    async def execute(
        self,
        stock_data_connector: IStockDataConnector,
        messaging_client: MessagingClient,
    ) -> None:
        get_quotations = await stock_data_connector.get_quotation()
        GenericNotFoundException.handle(
            get_quotations is None, "Not found any quotations."
        )

        for data in get_quotations["stocks"]:
            messaging_client.producer(
                exchange="get_quotations",
                routing_key="quotations.create",
                body=str(data)
            )
            logging.info(f"Sent message: {data}")
