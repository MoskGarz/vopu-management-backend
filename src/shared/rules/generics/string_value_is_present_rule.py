from typing import Any

from src.crosscuting.exception.vopu_exception import VopuException
from src.crosscuting.helpers.text_helper import TextHelper
from src.crosscuting.messages.technical_messages_enum import TechnicalMessagesEnum
from src.shared.rules.rule import Rule


class StringValueIsPresentRule(Rule):
    _EXPECTED_ARGS = 3

    @staticmethod
    def execute(*args: Any) -> None:
        if args is None or len(args) < StringValueIsPresentRule._EXPECTED_ARGS:
            raise VopuException.create(
                "infraestructura.rule.argumentos_invalidos",
                TechnicalMessagesEnum.RULE_STRING_VALUE_IS_PRESENT_ARGUMENTOS_INVALIDOS.value,
            )

        value: str = args[0]
        user_message_key: str = args[1]
        technical_message: str = args[2]
        apply_strip: bool = args[3] if len(args) > 3 else True

        if (
            TextHelper.is_empty_with_strip(value)
            if apply_strip
            else TextHelper.is_empty(value)
        ):
            raise VopuException.create(user_message_key, technical_message)
