from typing import List
import bcrypt
from application.dto.usuario.request.novo_usuario_request import NovoUsuarioRequest
from application.dto.usuario.response.novo_usuario_response import NovoUsuarioResponse
from domain.enums.usuario.usuario_padrao_enum import UsuarioPadraoEnum
from domain.exceptions.bad_request_exception import BadRequestException
from domain.exceptions.conflict_exception import ConflictException
from domain.models.usuario.usuario_model import UsuarioModel
from infrastructure.dao.postgres.usuario.usuario_dao import UsuarioDAO
from application.dto.usuario.response.listar_usuario_response import ListarUsuarioResponse, UsuarioDTO
from domain.validators.email_validator import EmailValidator

class UsuarioBO:
    def __init__(self):
        self.usuario_dao = UsuarioDAO()

    def _hash_password(self, password: str) -> str:
        """Gera hash da senha usando bcrypt"""
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')
    
    def _verify_password(self, password: str, hashed: str) -> bool:
        """Verifica se a senha corresponde ao hash"""
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

    async def novo_usuario(self, request : NovoUsuarioRequest):
        """Regra de negócio para criar novo usuário"""
        if not request.senha or len(request.senha) < 8:
            raise BadRequestException("Senha deve ter pelo menos 8 caracteres")
        
        email_valido, email_resultado = EmailValidator.validate_email_comprehensive(request.email)
        if not email_valido:
            raise BadRequestException(email_resultado)

        if request.senha != request.confirmar_senha:
            raise BadRequestException("Senhas não coincidem")
        
        usuario : UsuarioModel = await self.usuario_dao.buscar_por_email(email_resultado)

        if usuario:
            raise ConflictException("Email já cadastrado")

        request.senha = self._hash_password(request.senha)

        usuario_model = UsuarioModel(
            nome = request.nome,
            email = email_resultado,
            senha = request.senha
        )

        await self.usuario_dao.criar_novo_usuario(usuario_model, UsuarioPadraoEnum.ID.value)

        return NovoUsuarioResponse(email=email_resultado, nome=request.nome).to_dict()