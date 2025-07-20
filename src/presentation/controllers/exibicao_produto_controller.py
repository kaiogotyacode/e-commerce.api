from fastapi import Depends, HTTPException, status
from application.dto.exibicao.request.vincular_produto_exibicao_request import VincularProdutoExibicaoRequest
from domain.bo.exibicao_produto.exibicao_produto_bo import ExibicaoProdutoBO
from presentation.controllers.base_controller import BaseController
from domain.dependencies.usuario_bearer_token_dependency import validar_token_usuario

class ExibicaoProdutoController(BaseController):
        
    def __init__(self):
        super().__init__()
        self.exibicao_produto_bo = ExibicaoProdutoBO()

    async def vincular_produto_exibicao(self, request: VincularProdutoExibicaoRequest, id_usuario_logado: int = Depends(validar_token_usuario)):
        try:
            await self.exibicao_produto_bo.vincular_produto_exibicao(request, id_usuario_logado)
            return self._success_response(
                content=None,
                message="Produto vinculado com sucesso"
            )
        
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=self._handle_error(e, "Erro ao criar produto")
            )