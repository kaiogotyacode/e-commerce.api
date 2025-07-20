from fastapi import Depends, HTTPException, status
from application.dto.exibicao.request.vincular_produto_exibicao_request import VincularProdutoExibicaoRequest
from domain.bo.exibicao_produto.exibicao_produto_bo import ExibicaoProdutoBO
from presentation.controllers.base_controller import BaseController, handle_exceptions
from domain.dependencies.usuario_bearer_token_dependency import validar_token_usuario

class ExibicaoProdutoController(BaseController):
        
    def __init__(self):
        super().__init__()
        self.exibicao_produto_bo = ExibicaoProdutoBO()

    @handle_exceptions
    async def vincular_produto_exibicao(self, request: VincularProdutoExibicaoRequest, id_usuario_logado: int = Depends(validar_token_usuario)):
        await self.exibicao_produto_bo.vincular_produto_exibicao(request, id_usuario_logado)
        return self._success_response(
            content=None,
                message="Produto vinculado com sucesso"
            )