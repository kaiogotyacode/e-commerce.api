# src/presentation/routers/usuario_routes.py
from fastapi import APIRouter, Depends
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