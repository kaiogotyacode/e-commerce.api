from dataclasses import dataclass
from typing import Optional
from domain.models.common.base_model import BaseModel

@dataclass
class ExibicaoProdutoModel(BaseModel):
    id_exibicao_produto: Optional[int] = None
    id_exibicao: int = 0
    id_produto: int = 0
    order_list: Optional[int] = None