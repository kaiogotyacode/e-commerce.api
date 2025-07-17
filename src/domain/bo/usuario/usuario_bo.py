import bcrypt
from application.dto.usuario.request.novo_usuario_request import NovoUsuarioRequest
from application.dto.usuario.response.novo_usuario_response import NovoUsuarioResponse
from domain.enums.usuario.usuario_padrao_enum import UsuarioPadraoEnum
from domain.models.usuario.usuario_model import UsuarioModel
from infrastructure.dao.postgres.usuario.usuario_dao import UsuarioDAO

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
        if not request.senha or len(request.senha) < 6:
            raise ValueError("Senha deve ter pelo menos 6 caracteres")
        
        if not request.email or "@" not in request.email:
            raise ValueError("Email inválido")

        request.senha = self._hash_password(request.senha)

        usuario_model = UsuarioModel(
            nome = request.nome,
            email = request.email,
            senha = request.senha
        )

        await self.usuario_dao.criar_novo_usuario(usuario_model, UsuarioPadraoEnum.ID.value)

        return NovoUsuarioResponse(email=request.email, nome=request.nome).to_dict()