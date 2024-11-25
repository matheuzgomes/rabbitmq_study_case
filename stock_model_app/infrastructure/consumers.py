import threading

from stock_model_app.exception_handler import GlobalExceptionHandler
from stock_model_app.services.proccess_quotations_service import (
    ProcessQuotationsService,
)

from .messaging_client import MessagingClient


class Consumers:
    def load_quotations(self):
        try:
            client = MessagingClient("localhost")

            client.consumer(
                "post_quotations",
                ProcessQuotationsService().execute,
                "get_quotations",
                "quotations.create"
            )
        except Exception as error:
            raise GlobalExceptionHandler().handle(error) from error


    def start_consumer(self):
        consumer_thread = threading.Thread(target=self.load_quotations, daemon=True)
        consumer_thread.start()