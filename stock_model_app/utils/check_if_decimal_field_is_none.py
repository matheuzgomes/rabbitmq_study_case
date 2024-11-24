from typing import TypeVar
from decimal import Decimal


T = TypeVar("T")


class CheckDecimalFieldNullability:
    @staticmethod
    def execute(data: T) -> Decimal:
        if data is None:
            return 0.00
        return data
