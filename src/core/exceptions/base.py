from src.core.exceptions.error import BaseError

from http import HTTPStatus


NotFound = BaseError(HTTPStatus.NOT_FOUND, "Not Found.")
