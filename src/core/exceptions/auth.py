from .error import BaseError

IncorrectAuthorizationSchema = BaseError(
    401, "Incorrect authorization schema."
)
ExpiredToken = BaseError(401, "Invalid or expired token.")
InvalidToken = BaseError(401, "Invalid token authorization.")
IncorrectAuthorizeData = BaseError(400, "Incorrect password or ID.")
