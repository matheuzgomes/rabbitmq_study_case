class ServiceLayerException(Exception):
    @staticmethod
    def handle(case: bool, message: str):
        if case:
            raise ServiceLayerException(message)
