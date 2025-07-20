from domain.models.banner_produto.exibicao_produto_model import BannerProdutoModel
from infrastructure.dao.postgres.common.base_dao import BaseDAO

class BannerProdutoDAO(BaseDAO):

    @property
    def table_name(self) -> str:
        return "ecommerce.tbl_banner_produto"

    @property
    def model_class(self):
        return BannerProdutoModel

    @property
    def primary_key_field(self) -> str:
        return "id_banner_produto"

    async def criar_vinculo_banner_produto(self, model: BannerProdutoModel, id_usuario_logado: int) -> None:
        await self.criar(model, id_usuario_logado)

    async def validar_existencia_banner_produto(self, id_tipo_banner: int, id_produto: int, id_tela: int):
        query = f"""
                    SELECT 1 FROM {self.table_name}
                    WHERE id_tipo_banner = $1 AND id_produto = $2 AND id_tela = $3
                """

        params = (id_tipo_banner, id_produto, id_tela,)
        result = await self.execute_query(query, params)
        return True if result else False