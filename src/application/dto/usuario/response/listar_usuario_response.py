from typing import List
from application.dto.base_dto import BaseDTO

class UsuarioDTO(BaseDTO):
    nome: str = None
    email: str = None
    ativo: bool = True

class ListarUsuarioResponse(BaseDTO):
    usuarios : list[UsuarioDTO] = []