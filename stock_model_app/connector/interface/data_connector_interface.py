from abc import abstractmethod
from typing import Any


class IStockDataConnector:
    @abstractmethod
    async def get_quotation(self) -> Any:
        raise NotImplementedError("Method not implemented")
