from fastapi import HTTPException, status
from domain.exceptions.bad_request_exception import BadRequestException
from domain.exceptions.internal_server_exception import InternalServerException
from presentation.controllers.base_controller import BaseController
from domain.bo.usuario.usuario_bo import UsuarioBO
from application.dto.usuario.request.novo_usuario_request import NovoUsuarioRequest

class UsuarioController(BaseController):
        
    def __init__(self):
        super().__init__()
        self.usuario_bo = UsuarioBO()
    
    async def criar_usuario(self, request: NovoUsuarioRequest):
        try:
            resultado = await self.usuario_bo.novo_usuario(request)
            return self._success_response(
                data=resultado,
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
        
    async def autenticar_usuario(self, email: str, senha: str):
        try:
            resultado = await self.usuario_bo.autenticar_usuario(email, senha)
            return self._success_response(
                data=resultado,
                message="Autenticação realizada com sucesso"
            )
        
        except ValueError:
            raise BadRequestException("Requisição inválida.")
        
        except Exception:
            raise InternalServerException("Erro ao autenticar usuário.")