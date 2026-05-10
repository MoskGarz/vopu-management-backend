import re
from typing import Any

from src.crosscuting.exception.vopu_exception import VopuException
from src.crosscuting.helpers.text_helper import TextHelper
from src.crosscuting.messages.technical_messages_enum import TechnicalMessagesEnum
from src.shared.rules.rule import Rule


class StringFormatIsValidRule(Rule):
    _EXPECTED_ARGS = 4

    @staticmethod
    def execute(*args: Any) -> None:
        if args is None or len(args) < StringFormatIsValidRule._EXPECTED_ARGS:
            raise VopuException.create(
                "infraestructura.rule.argumentos_invalidos",
                TechnicalMessagesEnum.RULE_STRING_FORMAT_IS_VALID_ARGUMENTOS_INVALIDOS.value,
            )

        value: str = args[0]
        pattern: str = args[1]
        user_message_key: str = args[2]
        technical_message: str = args[3]
        apply_strip: bool = args[4] if len(args) > 4 else True

        safe_value = (
            TextHelper.get_default_with_strip(value)
            if apply_strip
            else TextHelper.get_default(value)
        )

        if not re.match(pattern, safe_value):
            raise VopuException.create(user_message_key, technical_message)
