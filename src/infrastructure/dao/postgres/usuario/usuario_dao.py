from domain.models.usuario.usuario_model import UsuarioModel
from infrastructure.dao.postgres.common.base_dao import BaseDAO
from typing import List, Optional

class UsuarioDAO(BaseDAO):

    @property
    def table_name(self) -> str:
        return "usuario.tbl_usuario"
    
    @property
    def model_class(self):
        return UsuarioModel
    
    @property
    def primary_key_field(self) -> str:
        return "id_usuario"
    
    async def criar_novo_usuario(self, model: UsuarioModel):
        """Método específico para criar usuário"""
        await self.criar(model)
    
    # Métodos específicos para UsuarioDAO (além dos herdados da BaseDAO)
    async def buscar_por_email(self, email: str) -> Optional[UsuarioModel]:
        """Busca um usuário pelo email"""
        usuarios = await self.buscar_por_filtro(email=email)
        return usuarios[0] if usuarios else None
    
    async def buscar_por_nome(self, nome: str) -> List[UsuarioModel]:
        """Busca usuários pelo nome"""
        return await self.buscar_por_filtro(nome=nome)
        