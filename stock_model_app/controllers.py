from ninja_extra import NinjaExtraAPI, api_controller, route

from stock_model_app.infrastructure import MessagingClient

from .connector.stock_data_connector import StockDataConnector
from .exception_handler import GlobalExceptionHandler
from .services import GetAllStocksService

app = NinjaExtraAPI()


@api_controller("/quotations")
class StockPriceController:
    def __init__(self) -> None:
        self.get_quotation_service = GetAllStocksService()

    @route.post(
        path="/",
        summary="Insert quotations",
        description="Insert quotations",
    )
    async def get_quotation(self):
        try:
            client = MessagingClient("localhost")
            data = await self.get_quotation_service.execute(
                stock_data_connector=StockDataConnector(),
                messaging_client=client,
            )

            return data
        except Exception as error:
            raise GlobalExceptionHandler().handle(error) from error

app.register_controllers(StockPriceController)
