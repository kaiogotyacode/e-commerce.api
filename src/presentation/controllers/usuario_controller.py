from fastapi import Depends
from presentation.controllers.base_controller import BaseController, handle_exceptions
from domain.bo.usuario.usuario_bo import UsuarioBO
from application.dto.usuario.request.novo_usuario_request import NovoUsuarioRequest
from domain.dependencies.usuario_bearer_token_dependency import validar_token_usuario

class UsuarioController(BaseController):
        
    def __init__(self):
        super().__init__()
        self.usuario_bo = UsuarioBO()
    
    @handle_exceptions
    async def criar_usuario(self, request: NovoUsuarioRequest):
        resultado = await self.usuario_bo.novo_usuario(request)
        return self._success_response(
            content=resultado,
            message="Usuário criado com sucesso"
        )

    # Método não faz sentido para E-commerce. Apenas para testar Bearer Token Validation
    @handle_exceptions
    async def listar_usuarios(self, token: str = Depends(validar_token_usuario)):
        resultado = await self.usuario_bo.listar_usuarios()
        return self._success_response(
            content=resultado,
            message="Action Succeeded"
        )