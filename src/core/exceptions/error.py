from typing import Any

_sentinel: Any = object()


class BaseError(Exception):
    def __init__(
        self, http_code: int, message: str, error: Exception = _sentinel
    ) -> None:
        self.http_code = http_code
        self.message = message
        self.error = error

    def __repr__(self) -> str:
        return self.message
