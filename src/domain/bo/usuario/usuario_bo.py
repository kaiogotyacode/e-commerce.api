from domain.dto.usuario.request import NovoUsuarioRequest
from domain.models.usuario.usuario_model import UsuarioModel
from infrastructure.dao.postgres.usuario.usuario_dao import UsuarioDAO

class UsuarioBO:
    def __init__(self):
        self.usuario_dao = UsuarioDAO()

    async def novo_usuario(self, request : NovoUsuarioRequest):
        usuario_model = UsuarioModel(
            nome = request.nome,
            email = request.email,
            senha = request.senha
        )

        await self.usuario_dao.criar_novo_usuario(usuario_model)

        return {"mensagem" : "Usuário criado com sucesso!"}