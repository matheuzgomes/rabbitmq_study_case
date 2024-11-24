from ninja_extra import NinjaExtraAPI, api_controller, route

from .connector.stock_data_connector import StockDataConnector
from .exception_handler import GlobalExceptionHandler
from .infrastructure import MessagingClient
from .services import GetAllStocksService, ProcessQuotationsService

app = NinjaExtraAPI()


@api_controller("/quotations")
class StockPriceController:
    def __init__(self) -> None:
        self.get_quotation_service = GetAllStocksService()
        self.messaging_client = MessagingClient("localhost")
        self.process_quotation_service = ProcessQuotationsService()

    @route.get(
        path="/",
        summary="Get quotations",
        description="Get quotations",
    )
    async def get_quotation(self):
        try:
            data = await self.get_quotation_service.execute(
                stock_data_connector=StockDataConnector(),
                messaging_client=self.messaging_client,
            )

            return data
        except Exception as error:
            raise GlobalExceptionHandler().handle(error) from error

    @route.post(
        path="/",
        summary="Insert quotations",
        description="Insert quotations",
    )
    def load_quotations(self):
        try:
            self.messaging_client.consumer(
                "post_quotations",
                self.process_quotation_service.execute,
                "get_quotations",
                "quotations.create",
            )
            return {"ok": 200}
        except Exception as error:
            raise GlobalExceptionHandler().handle(error) from error


app.register_controllers(StockPriceController)
