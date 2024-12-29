from http import HTTPStatus

from .error import BaseError

IncorrectAuthorizationSchema = BaseError(
    HTTPStatus.UNAUTHORIZED, "Incorrect authorization schema."
)
ExpiredToken = BaseError(HTTPStatus.UNAUTHORIZED, "Invalid or expired token.")
InvalidToken = BaseError(
    HTTPStatus.UNAUTHORIZED, "Invalid token authorization."
)
IncorrectAuthorizeData = BaseError(
    HTTPStatus.BAD_REQUEST, "Incorrect password or ID."
)
