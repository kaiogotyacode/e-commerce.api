from typing import Optional
from application.dto.base_dto import BaseDTO

class VinculoProdutoExibicao(BaseDTO):
    local: Optional[str] = None
    descricao: Optional[float] = None
    valor_unitario: Optional[str] = None
    img_url: Optional[str] = None

class RetornarVinculoProdutoExibicaoResponse(BaseDTO):
    vinculos : Optional[list[VinculoProdutoExibicao]] = None
