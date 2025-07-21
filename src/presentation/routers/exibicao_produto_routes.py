# src/presentation/routers/usuario_routes.py
from fastapi import APIRouter, Depends
from application.dto.exibicao_produto.request.vincular_produto_exibicao_request import VincularProdutoExibicaoRequest
from domain.dependencies.usuario_bearer_token_dependency import validar_token_usuario
from presentation.controllers.exibicao_produto_controller import ExibicaoProdutoController

router = APIRouter(
    prefix="/exibicao_produto",
    tags=["Exibição de Produtos"]
)

exibicao_produto_controller = ExibicaoProdutoController()

@router.post("/vincular_produto_exibicao", response_model=None)
async def vincular_produto_exibicao(request: VincularProdutoExibicaoRequest, id_usuario_logado: int = Depends(validar_token_usuario)):
    """
    Vincular um produto a uma exibição.

    - **id_produto**: ID do produto a ser vinculado
    - **id_exibicao**: ID da exibição onde o produto será vinculado
    - **order_list**: Ordem de exibição do produto na exibição
    """
    return await exibicao_produto_controller.vincular_produto_exibicao(request, id_usuario_logado)