from typing import Any

from src.crosscuting.exception.vopu_exception import VopuException
from src.crosscuting.helpers.text_helper import TextHelper
from src.crosscuting.messages.technical_messages_enum import TechnicalMessagesEnum
from src.shared.rules.rule import Rule


class StringLengthIsValidRule(Rule):
    _EXPECTED_ARGS = 5

    @staticmethod
    def execute(*args: Any) -> None:
        if args is None or len(args) < StringLengthIsValidRule._EXPECTED_ARGS:
            raise VopuException.create(
                "infraestructura.rule.argumentos_invalidos",
                TechnicalMessagesEnum.RULE_STRING_LENGTH_IS_VALID_ARGUMENTOS_INVALIDOS.value,
            )

        value: str = args[0]
        min_length: int = args[1]
        max_length: int = args[2]
        user_message_key: str = args[3]
        technical_message: str = args[4]
        apply_strip: bool = args[5] if len(args) > 5 else True

        if not TextHelper.is_length_valid(value, min_length, max_length, apply_strip):
            raise VopuException.create(user_message_key, technical_message)
