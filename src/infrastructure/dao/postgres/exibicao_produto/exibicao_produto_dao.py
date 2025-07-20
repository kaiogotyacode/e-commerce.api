from domain.models.exibicao_produto.exibicao_produto_model import ExibicaoProdutoModel
from infrastructure.dao.postgres.common.base_dao import BaseDAO

class ExibicaoProdutoDAO(BaseDAO):

    @property
    def table_name(self) -> str:
        return "ecommerce.tbl_exibicao_produto"

    @property
    def model_class(self):
        return ExibicaoProdutoModel

    @property
    def primary_key_field(self) -> str:
        return "id_exibicao_produto"

    async def criar_vinculo_exibicao_produto(self, model: ExibicaoProdutoModel, id_usuario_logado: int) -> None:
        await self.criar(model, id_usuario_logado)

    async def validar_existencia_produto_exibicao(self, id_exibicao: int, id_produto: int):
        query = f"""
                    SELECT 1 FROM {self.table_name}
                    WHERE id_exibicao = $1 AND id_produto = $2
                """

        params = (id_exibicao, id_produto,)
        result = await self.execute_query(query, params)
        return True if result else False