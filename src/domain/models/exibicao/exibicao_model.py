from dataclasses import dataclass
from typing import Optional
from domain.enums.usuario.usuario_padrao_enum import UsuarioPadraoEnum
from domain.models.common.base_model import BaseModel

@dataclass
class ExibicaoModel(BaseModel):
    id_exibicao: Optional[int] = None
    id_local_exibicao: int = 0