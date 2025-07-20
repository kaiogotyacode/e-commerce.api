from typing import Optional
from application.dto.base_dto import BaseDTO

class NovoProdutoResponse(BaseDTO):
    descricao: Optional[str] = None
    valor_unitario: Optional[float] = None
    img_url: Optional[str] = None
