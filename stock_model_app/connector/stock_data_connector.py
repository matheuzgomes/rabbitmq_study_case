import os
from dataclasses import dataclass, field
from typing import Any

import requests

from ..utils import Constants
from .interface import IStockDataConnector


@dataclass
class StockDataConnector(IStockDataConnector):
    base_url: str = Constants.brapi_dev_url
    authentication_header: dict[str, str] = field(
        default_factory=lambda: {"Authorization": f"Bearer {os.getenv('BR_API_TOKEN')}"}
    )

    async def get_quotation(self) -> Any:
        try:
            request = requests.get(
                f"{self.base_url}/quote/list", headers=self.authentication_header
            )
            return request.json()
        except Exception as error:
            raise Exception(error)
