from dataclasses import dataclass
from typing import Optional
from domain.enums.usuario.usuario_padrao_enum import UsuarioPadraoEnum
from domain.models.common.base_model import BaseModel

@dataclass
class UsuarioModel(BaseModel):
    id_usuario: Optional[int] = None
    nome: str = ""
    email: str = ""
    senha: str = ""
    ativo: bool = True

    def is_novo_usuario(self) -> bool:
        """Verifica se é um novo usuário"""
        return self.is_novo_registro("id_usuario")