from dataclasses import dataclass
from typing import Optional
from domain.models.common.base_model import BaseModel

@dataclass
class BannerProdutoModel(BaseModel):
    id_banner_produto: Optional[int] = None
    id_tipo_banner: int = 0
    id_tela: int = 0
    id_produto: int = 0
    order_list: Optional[int] = None