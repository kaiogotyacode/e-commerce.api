from application.dto.exibicao.response.retornar_vinculo_produto_exibicao_dto import RetornarVinculoProdutoExibicaoResponse, VinculoProdutoExibicao
from domain.models.exibicao.exibicao_produto_model import ExibicaoProdutoModel
from infrastructure.dao.postgres.common.base_dao import BaseDAO

class ExibicaoProdutoDAO(BaseDAO):

    @property
    def table_name(self) -> str:
        return "ecommerce.tbl_exibicao_produto"

    @property
    def model_class(self):
        return ExibicaoProdutoModel

    @property
    def vinc_prod_exib(self):
        return RetornarVinculoProdutoExibicaoResponse

    @property
    def primary_key_field(self) -> str:
        return "id_exibicao_produto"

    async def criar_vinculo_exibicao_produto(self, model: ExibicaoProdutoModel, id_usuario_logado: int) -> None:
        await self.criar(model, id_usuario_logado)

    # async def retornar_vinculo_produto_exibicao(self):
    #     query = f"""
    #                 QUERY
    #             """

    #     params = (None,)
    #     result = await self.execute_query(query, params)
    #     return self.model_class(**result[0]) if result else None