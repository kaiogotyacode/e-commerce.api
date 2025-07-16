from fastapi import HTTPException, status
from presentation.controllers.base_controller import BaseController
from domain.bo.auth.auth_bo import AuthBO
from application.dto.auth.request.autenticar_usuario_request import AutenticarUsuarioRequest

class TokenController(BaseController):
        
    def __init__(self):
        super().__init__()
        self.auth_bo = AuthBO()
    
    async def autenticar_usuario(self, request: AutenticarUsuarioRequest):
        try:
            resultado = await self.auth_bo.autenticar_usuario(request)
            return self._success_response(
                data=resultado,
                message="Autenticação realizada com sucesso"
            )
        
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=self._handle_error(e, "Erro ao autenticar usuário")
            )