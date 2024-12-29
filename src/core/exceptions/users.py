from http import HTTPStatus

from .error import BaseError

UserAlreadyExists = BaseError(HTTPStatus.BAD_REQUEST, "User already exists")
UserNotExists = BaseError(HTTPStatus.BAD_REQUEST, "User does not exists.")
