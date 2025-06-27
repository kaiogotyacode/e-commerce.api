from dataclasses import dataclass

@dataclass
class UsuarioModel:
    nome : str
    email : str
    senha : str