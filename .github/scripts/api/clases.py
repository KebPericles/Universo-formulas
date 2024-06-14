
class Formula:
    def __init__(
        self,
        nombre: str,
        aliases: list[str],
        referencias: list[str],
        codigo: str,
        contenido_bruto: str,
        otras_formulas: list[str],
    ):
        self.nombre = nombre
        self.aliases = aliases
        self.referencias = referencias
        self.codigo = codigo
        self.contenido_bruto = contenido_bruto
        self.otras_formulas = otras_formulas

class Subtema:
    def __init__(
        self,
        nombre: str,
        aliases: list[str],
        referencias: list[str],
        formulas: list[Formula]
    ):
        self.nombre = nombre
        self.aliases = aliases
        self.referencias = referencias
        self.formulas = formulas

class Formulario:
    def __init__(
        self,
        uuid: str,
        nombre: str,
        aliases: list[str],
        temas_relacionados: list[str],
        metadatos: dict[str, any],
        referencias: list[str],
        subtemas: list[Subtema]
    ):
        self.uuid = uuid
        self.nombre = nombre
        self.aliases = aliases
        self.temas_relacionados = temas_relacionados
        self.metadatos = metadatos
        self.referencias = referencias
        self.subtemas = subtemas