# src/presentation/routers/usuario_routes.py
from fastapi import APIRouter, Depends
from application.dto.banner_produto.request.vincular_produto_banner_request import VincularProdutoBannerRequest
from application.dto.exibicao_produto.request.vincular_produto_exibicao_request import VincularProdutoExibicaoRequest
from domain.dependencies.usuario_bearer_token_dependency import validar_token_usuario
from presentation.controllers.banner_produto_controller import BannerProdutoController
from presentation.controllers.exibicao_produto_controller import ExibicaoProdutoController

router = APIRouter(
    prefix="/banner_produto",
    tags=["Banner de Produtos"]
)

banner_produto_controller = BannerProdutoController()

@router.post("/vincular_produto_banner", response_model=None)
async def vincular_produto_banner(request: VincularProdutoBannerRequest, id_usuario_logado: int = Depends(validar_token_usuario)):
    """
    Vincular um produto a um banner.
    """
    return await banner_produto_controller.vincular_produto_banner(request, id_usuario_logado)