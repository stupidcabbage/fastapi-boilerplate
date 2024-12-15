from .error import BaseError

UserAlreadyExists = BaseError(400, "User already exists", Exception())
