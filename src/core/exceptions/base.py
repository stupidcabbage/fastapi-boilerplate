from http import HTTPStatus

from src.core.exceptions.error import BaseError

NotFound = BaseError(HTTPStatus.NOT_FOUND, "Not Found.")
