from typing import final

from src.crosscuting.helpers.text_helper import TextHelper


@final
class VopuException(Exception):
    def __init__(
        self,
        user_message_key: str,
        technical_message: str,
        cause: Exception | None = None,
    ) -> None:
        super().__init__(technical_message)
        self._user_message_key = TextHelper.get_default_with_strip(user_message_key)
        self._technical_message = TextHelper.get_default_with_strip(technical_message)
        self._cause = cause if cause is not None else Exception()

    @staticmethod
    def create(
        user_message_key: str, technical_message: str, cause: Exception | None = None
    ) -> "VopuException":
        return VopuException(user_message_key, technical_message, cause)

    @property
    def user_message_key(self) -> str:
        return self._user_message_key

    @property
    def technical_message(self) -> str:
        return self._technical_message

    @property
    def cause(self) -> Exception:
        return self._cause
