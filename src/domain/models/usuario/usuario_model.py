from dataclasses import dataclass
from typing import Optional

@dataclass
class UsuarioModel:
    nome: str
    email: str
    senha: str
    id_usuario: Optional[int] = None