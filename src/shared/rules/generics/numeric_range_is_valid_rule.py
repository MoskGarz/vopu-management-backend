from typing import Any

from src.crosscuting.exception.vopu_exception import VopuException
from src.crosscuting.helpers.int_helper import IntHelper
from src.crosscuting.messages.technical_messages_enum import TechnicalMessagesEnum
from src.shared.rules.rule import Rule


class NumericRangeIsValidRule(Rule):
    _EXPECTED_ARGS = 5

    @staticmethod
    def execute(*args: Any) -> None:
        if args is None or len(args) < NumericRangeIsValidRule._EXPECTED_ARGS:
            raise VopuException.create(
                "infraestructura.rule.argumentos_invalidos",
                TechnicalMessagesEnum.RULE_NUMERIC_RANGE_IS_VALID_ARGUMENTOS_INVALIDOS.value,
            )

        value: int = args[0]
        min_value: int = args[1]
        max_value: int = args[2]
        user_message_key: str = args[3]
        technical_message: str = args[4]

        if not IntHelper.is_range_valid(value, min_value, max_value):
            raise VopuException.create(user_message_key, technical_message)
