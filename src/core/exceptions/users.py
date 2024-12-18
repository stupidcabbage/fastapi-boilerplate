from .error import BaseError

UserAlreadyExists = BaseError(400, "User already exists")
UserNotExists = BaseError(400, "User does not exists.")
