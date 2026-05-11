from src.crosscuting.helpers.text_helper import TextHelper


class AddClienteDTO:
    def __init__(
        self, numero_documento: str = "", nombre_completo: str = "", telefono: str = ""
    ) -> None:
        self._numero_documento = TextHelper.get_default_with_strip(numero_documento)
        self._nombre_completo = TextHelper.get_default_with_strip(nombre_completo)
        self._telefono = TextHelper.get_default_with_strip(telefono)

    @property
    def numero_documento(self) -> str:
        return self._numero_documento

    @property
    def nombre_completo(self) -> str:
        return self._nombre_completo

    @property
    def telefono(self) -> str:
        return self._telefono
