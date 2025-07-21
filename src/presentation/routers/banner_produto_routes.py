# src/presentation/routers/usuario_routes.py
from fastapi import APIRouter, Depends
from application.dto.banner_produto.request.vincular_produto_banner_request import VincularProdutoBannerRequest
from domain.dependencies.usuario_bearer_token_dependency import validar_token_usuario
from presentation.controllers.banner_produto_controller import BannerProdutoController

router = APIRouter(
    prefix="/banner_produto",
    tags=["Banner de Produtos"]
)

banner_produto_controller = BannerProdutoController()

@router.post("/vincular_produto_banner", response_model=None)
async def vincular_produto_banner(request: VincularProdutoBannerRequest, id_usuario_logado: int = Depends(validar_token_usuario)):
    """
    Vincular um produto a um banner.

    - **id_produto**: ID do produto a ser vinculado
    - **id_tipo_banner**: ID do tipo de banner onde o produto será vinculado
    - **id_tela**: ID da tela onde o produto será vinculado
    - **order_list**: Ordem de exibição do produto no banner
    """
    return await banner_produto_controller.vincular_produto_banner(request, id_usuario_logado)