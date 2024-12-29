from .error import BaseError

from http import HTTPStatus

UserAlreadyExists = BaseError(HTTPStatus.BAD_REQUEST, "User already exists")
UserNotExists = BaseError(HTTPStatus.BAD_REQUEST, "User does not exists.")
