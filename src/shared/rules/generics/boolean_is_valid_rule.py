from typing import Any

from src.crosscuting.exception.vopu_exception import VopuException
from src.crosscuting.messages.technical_messages_enum import TechnicalMessagesEnum
from src.shared.rules.rule import Rule


class BooleanIsValidRule(Rule):
    _EXPECTED_ARGS = 3

    @staticmethod
    def execute(*args: Any) -> None:
        if args is None or len(args) < BooleanIsValidRule._EXPECTED_ARGS:
            raise VopuException.create(
                "infraestructura.rule.argumentos_invalidos",
                TechnicalMessagesEnum.RULE_BOOLEAN_IS_VALID_ARGUMENTOS_INVALIDOS.value,
            )

        value: bool = args[0]
        user_message_key: str = args[1]
        technical_message: str = args[2]

        if value is None:
            raise VopuException.create(user_message_key, technical_message)
