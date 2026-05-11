from typing import final

from src.crosscuting.messages.technical_messages_enum import TechnicalMessagesEnum
from src.features.cliente.add_cliente.application.use_case.domain.add_cliente_domain import (
    AddClienteDomain,
)
from src.shared.rules.generics.string_format_is_valid_rule import (
    StringFormatIsValidRule,
)
from src.shared.rules.generics.string_length_is_valid_rule import (
    StringLengthIsValidRule,
)
from src.shared.rules.generics.string_value_is_present_rule import (
    StringValueIsPresentRule,
)


@final
class ValidateAddClienteDataConsistency:
    def __init__(self) -> None:
        raise RuntimeError("ValidateAddClienteDataConsistency no puede ser instanciado")

    @staticmethod
    def validate(domain: AddClienteDomain) -> None:
        ValidateAddClienteDataConsistency._validate_numero_documento(domain)
        ValidateAddClienteDataConsistency._validate_nombre_completo(domain)
        ValidateAddClienteDataConsistency._validate_telefono(domain)

    @staticmethod
    def _validate_numero_documento(domain: AddClienteDomain) -> None:
        StringValueIsPresentRule.execute(
            domain.numero_documento,
            "cliente.documento.invalido",
            TechnicalMessagesEnum.CLIENTE_DOCUMENTO_INVALIDO.value,
        )
        StringLengthIsValidRule.execute(
            domain.numero_documento,
            7,
            10,
            "cliente.documento.longitud.invalida",
            TechnicalMessagesEnum.CLIENTE_DOCUMENTO_LONGITUD_INVALIDA.value,
        )
        StringFormatIsValidRule.execute(
            domain.numero_documento,
            r"^\d{7,10}$",
            "cliente.documento.formato.invalido",
            TechnicalMessagesEnum.CLIENTE_DOCUMENTO_FORMATO_INVALIDO.value,
        )

    @staticmethod
    def _validate_nombre_completo(domain: AddClienteDomain) -> None:
        StringValueIsPresentRule.execute(
            domain.nombre_completo,
            "cliente.nombre_completo.invalido",
            TechnicalMessagesEnum.CLIENTE_NOMBRE_COMPLETO_INVALIDO.value,
        )
        StringLengthIsValidRule.execute(
            domain.nombre_completo,
            2,
            50,
            "cliente.nombre_completo.longitud.invalida",
            TechnicalMessagesEnum.CLIENTE_NOMBRE_COMPLETO_LONGITUD_INVALIDA.value,
        )
        StringFormatIsValidRule.execute(
            domain.nombre_completo,
            r"^[A-Za-záéíóúÁÉÍÓÚñÑüÜ'\-\s]+$",
            "cliente.nombre_completo.formato.invalido",
            TechnicalMessagesEnum.CLIENTE_NOMBRE_COMPLETO_FORMATO_INVALIDO.value,
        )

    @staticmethod
    def _validate_telefono(domain: AddClienteDomain) -> None:
        StringValueIsPresentRule.execute(
            domain.telefono,
            "cliente.telefono.invalido",
            TechnicalMessagesEnum.CLIENTE_TELEFONO_INVALIDO.value,
        )
        StringLengthIsValidRule.execute(
            domain.telefono,
            10,
            10,
            "cliente.telefono.longitud.invalida",
            TechnicalMessagesEnum.CLIENTE_TELEFONO_LONGITUD_INVALIDA.value,
        )
        StringFormatIsValidRule.execute(
            domain.telefono,
            r"^\d{10}$",
            "cliente.telefono.formato.invalido",
            TechnicalMessagesEnum.CLIENTE_TELEFONO_FORMATO_INVALIDO.value,
        )
