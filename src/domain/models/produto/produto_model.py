from dataclasses import dataclass
from typing import Optional
from domain.models.common.base_model import BaseModel

@dataclass
class ProdutoModel(BaseModel):
    id_produto: Optional[int] = None
    descricao: str = ""
    valor_unitario: float = 0.0
    img_url: str = ""