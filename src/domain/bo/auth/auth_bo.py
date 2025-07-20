import bcrypt
from application.dto.auth.request.autenticar_usuario_request import AutenticarUsuarioRequest
from domain.models.usuario.usuario_model import UsuarioModel
from infrastructure.dao.postgres.auth.auth_dao import AuthDAO
from domain.bo.auth.jwt_manager import JWTManager
from domain.validators.email_validator import EmailValidator

class AuthBO:
    def __init__(self):
        self.auth_dao = AuthDAO()
        self.jwt_manager = JWTManager()

    def _hash_password(self, password: str) -> str:
        """Gera hash da senha usando bcrypt"""
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')
    
    def _verify_password(self, password: str, hashed: str) -> bool:
        """Verifica se a senha corresponde ao hash"""
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

    async def autenticar_usuario(self, request : AutenticarUsuarioRequest):
        email_normalizado = EmailValidator.normalize_email(request.email)
        
        usuario : UsuarioModel = await self.auth_dao.buscar_por_email(email_normalizado)

        if not usuario:
            raise ValueError("Usuário não encontrado ou credenciais inválidas!")

        if not self._verify_password(request.senha, usuario.senha):
            raise ValueError("Usuário não encontrado ou credenciais inválidas!")

        if not usuario.ativo:
            raise ValueError("Usuário inativo. Por favor, ative sua conta antes de tentar autenticar.")
    
        return self.jwt_manager.generate_token(usuario.id_usuario)
