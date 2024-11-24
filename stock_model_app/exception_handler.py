from http import HTTPStatus

from django.db.utils import IntegrityError
from ninja.errors import HttpError

from .utils import GenericNotFoundException, ServiceLayerException


class GlobalExceptionHandler(BaseException):
    def __init__(self) -> None:
        self.errors_dict = {
            IntegrityError: HTTPStatus.BAD_REQUEST,
            GenericNotFoundException: HTTPStatus.BAD_REQUEST,
            ServiceLayerException: HTTPStatus.BAD_REQUEST,
        }

    def handle(self, error: Exception):
        status_code = self.errors_dict.get(type(error))

        if status_code:
            raise HttpError(status_code, str(error))
