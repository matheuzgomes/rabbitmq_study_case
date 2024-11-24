class GenericNotFoundException(Exception):
    @staticmethod
    def handle(case: bool, message: str):
        if case:
            raise GenericNotFoundException(message)
