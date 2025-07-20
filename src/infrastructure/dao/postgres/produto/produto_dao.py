from domain.models.produto.produto_model import ProdutoModel
from infrastructure.dao.postgres.common.base_dao import BaseDAO
from typing import List, Optional

class ProdutoDAO(BaseDAO):

    @property
    def table_name(self) -> str:
        return "ecommerce.tbl_produto"

    @property
    def model_class(self):
        return ProdutoModel

    @property
    def primary_key_field(self) -> str:
        return "id_produto"

    async def criar_novo_produto(self, model: ProdutoModel, usuario_id: int = None):
        """Método específico para criar produto"""
        await self.criar(model, usuario_id)

    async def buscar_por_id(self, id_produto: int) -> Optional[ProdutoModel]:
        produto = await self.buscar_por_filtro(id_produto=id_produto)
        return produto[0] if produto else None
