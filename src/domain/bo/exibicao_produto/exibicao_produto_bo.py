from typing import List
import bcrypt
from application.dto.exibicao.request.vincular_produto_exibicao_request import VincularProdutoExibicaoRequest
from application.dto.produto.request.novo_produto_request import NovoProdutoRequest
from application.dto.produto.response.novo_produto_response import NovoProdutoResponse
from domain.models.exibicao.exibicao_produto_model import ExibicaoProdutoModel
from domain.models.produto.produto_model import ProdutoModel
from infrastructure.dao.postgres.exibicao.exibicao_produto_dao import ExibicaoProdutoDAO


class ExibicaoProdutoBO:
    def __init__(self):
        self.exibicao_produto_dao = ExibicaoProdutoDAO()

    async def vincular_produto_exibicao(self, request : VincularProdutoExibicaoRequest, id_usuario_logado : int):
        #TODO: Validações idProduto | idExibição | or isAdmin

        exibicao_produto_model = ExibicaoProdutoModel(
            id_exibicao=request.id_exibicao,
            id_produto=request.id_produto,
            order_list=request.order_list
        )
    
        await self.exibicao_produto_dao.criar_vinculo_exibicao_produto(exibicao_produto_model, id_usuario_logado)