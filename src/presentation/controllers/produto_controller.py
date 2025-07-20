from fastapi import Depends, HTTPException, status
from application.dto.produto.request.novo_produto_request import NovoProdutoRequest
from domain.bo.produto.produto_bo import ProdutoBO
from presentation.controllers.base_controller import BaseController
from domain.bo.usuario.usuario_bo import UsuarioBO
from application.dto.usuario.request.novo_usuario_request import NovoUsuarioRequest
from domain.dependencies.usuario_bearer_token_dependency import validar_token_usuario

class ProdutoController(BaseController):
        
    def __init__(self):
        super().__init__()
        self.produto_bo = ProdutoBO()

    async def cadastrar_novo_produto(self, request: NovoProdutoRequest, id_usuario_logado: int = Depends(validar_token_usuario)):
        try:
            resultado = await self.produto_bo.novo_produto(request, id_usuario_logado)
            return self._success_response(
                content=resultado,
                message="Produto criado com sucesso"
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