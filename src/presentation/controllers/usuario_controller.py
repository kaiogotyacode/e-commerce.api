from fastapi import Depends, HTTPException, status
from presentation.controllers.base_controller import BaseController
from domain.bo.usuario.usuario_bo import UsuarioBO
from application.dto.usuario.request.novo_usuario_request import NovoUsuarioRequest
from domain.dependencies.usuario_bearer_token_dependency import validar_token_usuario

class UsuarioController(BaseController):
        
    def __init__(self):
        super().__init__()
        self.usuario_bo = UsuarioBO()
    
    async def criar_usuario(self, request: NovoUsuarioRequest):
        try:
            resultado = await self.usuario_bo.novo_usuario(request)
            return self._success_response(
                content=resultado,
                message="Usuário criado com sucesso"
            )
        
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=self._handle_error(e, "Erro ao criar usuário")
            )

    # Método não faz sentido para E-commerce. Apenas para testar Bearer Token Validation
    async def listar_usuarios(self, token: str = Depends(validar_token_usuario)):
        try:
            resultado = await self.usuario_bo.listar_usuarios()
            return self._success_response(
                content=resultado,
                message="Action Succeeded"
            )
        
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=self._handle_error(e, "Erro ao listar usuários")
            )