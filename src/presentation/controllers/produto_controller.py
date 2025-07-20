from fastapi import Depends
from application.dto.produto.request.novo_produto_request import NovoProdutoRequest
from domain.bo.produto.produto_bo import ProdutoBO
from presentation.controllers.base_controller import BaseController, handle_exceptions
from domain.bo.usuario.usuario_bo import UsuarioBO
from domain.dependencies.usuario_bearer_token_dependency import validar_token_usuario

class ProdutoController(BaseController):
        
    def __init__(self):
        super().__init__()
        self.produto_bo = ProdutoBO()

    @handle_exceptions
    async def cadastrar_novo_produto(self, request: NovoProdutoRequest, id_usuario_logado: int = Depends(validar_token_usuario)):
        resultado = await self.produto_bo.novo_produto(request, id_usuario_logado)
        return self._success_response(
            content=resultado,
            message="Produto criado com sucesso"
        )