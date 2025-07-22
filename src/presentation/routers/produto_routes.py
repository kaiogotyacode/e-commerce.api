# src/presentation/routers/usuario_routes.py
from fastapi import APIRouter, Depends
from application.dto.banner_produto.request.vincular_produto_banner_request import VincularProdutoBannerRequest
from application.dto.exibicao_produto.request.vincular_produto_exibicao_request import VincularProdutoExibicaoRequest
from application.dto.produto.request.novo_produto_request import NovoProdutoRequest
from domain.dependencies.usuario_bearer_token_dependency import validar_token_usuario
from presentation.controllers.produto_controller import ProdutoController

router = APIRouter(
    prefix="/produto",
    tags=["Produtos"]
)

produto_controller = ProdutoController()

@router.post("/novo_produto", response_model=None)
async def cadastrar_novo_produto(request: NovoProdutoRequest, id_usuario_logado: int = Depends(validar_token_usuario)):
    """
    Cadastrar um novo produto no sistema.

    - **descricao**: Descrição do produto
    - **img_url**: URL da imagem do produto
    - **valor_unitario**: Valor unitário do produto
    """
    return await produto_controller.cadastrar_novo_produto(request, id_usuario_logado)


@router.post("/vincular_produto_exibicao", response_model=None)
async def vincular_produto_exibicao(request: VincularProdutoExibicaoRequest, id_usuario_logado: int = Depends(validar_token_usuario)):
    """
    Vincular um produto a uma exibição.

    - **id_produto**: ID do produto a ser vinculado
    - **id_exibicao**: ID da exibição onde o produto será vinculado
    - **order_list**: Ordem de exibição do produto na exibição
    """
    return await produto_controller.vincular_produto_exibicao(request, id_usuario_logado)


@router.post("/vincular_produto_banner", response_model=None)
async def vincular_produto_banner(request: VincularProdutoBannerRequest, id_usuario_logado: int = Depends(validar_token_usuario)):
    """
    Vincular um produto a um banner.

    - **id_produto**: ID do produto a ser vinculado
    - **id_tipo_banner**: ID do tipo de banner onde o produto será vinculado
    - **id_tela**: ID da tela onde o produto será vinculado
    - **order_list**: Ordem de exibição do produto no banner
    """
    return await produto_controller.vincular_produto_banner(request, id_usuario_logado)