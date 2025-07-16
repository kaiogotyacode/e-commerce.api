from domain.models.usuario.usuario_model import UsuarioModel
from infrastructure.dao.postgres.common.base_dao import BaseDAO
from typing import Optional

class AuthDAO(BaseDAO):

    @property
    def table_name(self) -> str:
        return "usuarios.tbl_usuario"
    
    @property
    def model_class(self):
        return UsuarioModel
    
    @property
    def primary_key_field(self) -> str:
        return "id_usuario"
        
    async def buscar_por_email(self, email: str) -> Optional[UsuarioModel]:
        query = """
                    SELECT  tu.id_usuario, 
                            tu.nome, 
                            tu.email, 
                            tu.senha, 
                            tu.ativo
                    FROM usuarios.tbl_usuario tu
                    WHERE tu.email = %s AND tu.ativo = true"""

        params = (email,)
        result = await self.execute_query(query, params)
        return self.model_class(**result[0]) if result else None