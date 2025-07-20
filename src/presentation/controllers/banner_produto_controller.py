from fastapi import Depends
from application.dto.banner_produto.request.vincular_produto_banner_request import VincularProdutoBannerRequest
from domain.bo.banner_produto.banner_produto_bo import BannerProdutoBO
from presentation.controllers.base_controller import BaseController, handle_exceptions
from domain.dependencies.usuario_bearer_token_dependency import validar_token_usuario

class BannerProdutoController(BaseController):
        
    def __init__(self):
        super().__init__()
        self.banner_produto_bo = BannerProdutoBO()

    @handle_exceptions
    async def vincular_produto_banner(self, request: VincularProdutoBannerRequest, id_usuario_logado: int = Depends(validar_token_usuario)):
        await self.banner_produto_bo.vincular_produto_banner(request, id_usuario_logado)
        return self._success_response(
            content=None,
                message="Produto vinculado com sucesso"
            )