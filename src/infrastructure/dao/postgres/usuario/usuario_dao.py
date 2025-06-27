from domain.models.usuario.usuario_model import UsuarioModel
import asyncpg

class UsuarioDAO:

    def __init__(self):
        self.dsn = "postgresql://neondb_owner:npg_Xpi4jSxqdM3R@ep-ancient-glade-a87hrwfe-pooler.eastus2.azure.neon.tech/neondb?sslmode=require&channel_binding=require"

    async def criar_novo_usuario(self, model : UsuarioModel):
        conn = await asyncpg.connect(dsn=self.dsn)
        try:
            await conn.execute("""
                INSERT INTO usuario.tbl_usuario (nome, email, senha)
                VALUES ($1, $2, $3)
            """, model.nome, model.email, model.senha)

        finally:
            await conn.close()
        