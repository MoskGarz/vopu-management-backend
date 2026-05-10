from typing import Any
from uuid import UUID

from src.crosscuting.exception.vopu_exception import VopuException
from src.crosscuting.helpers.uuid_helper import UUIDHelper
from src.crosscuting.messages.technical_messages_enum import TechnicalMessagesEnum
from src.shared.rules.rule import Rule


class IdIsNotDefaultRule(Rule):
    _EXPECTED_ARGS = 3

    @staticmethod
    def execute(*args: Any) -> None:
        if args is None or len(args) < IdIsNotDefaultRule._EXPECTED_ARGS:
            raise VopuException.create(
                "infraestructura.rule.argumentos_invalidos",
                TechnicalMessagesEnum.RULE_ID_IS_NOT_DEFAULT_ARGUMENTOS_INVALIDOS.value,
            )

        value: UUID = args[0]
        user_message_key: str = args[1]
        technical_message: str = args[2]

        if UUIDHelper.is_default_uuid(value):
            raise VopuException.create(user_message_key, technical_message)
