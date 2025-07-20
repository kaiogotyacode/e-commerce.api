from typing import List
import bcrypt
from application.dto.produto.request.novo_produto_request import NovoProdutoRequest
from application.dto.produto.response.novo_produto_response import NovoProdutoResponse
from domain.models.produto.produto_model import ProdutoModel
from infrastructure.dao.postgres.produto.produto_dao import ProdutoDAO


class ProdutoBO:
    def __init__(self):
        self.produto_dao = ProdutoDAO()

    async def novo_produto(self, request : NovoProdutoRequest, id_usuario_logado : int) -> NovoProdutoResponse:
        if not request.descricao or len(request.descricao) < 3:
            raise ValueError("Descrição deve ter pelo menos 3 caracteres")

        if not request.valor_unitario or request.valor_unitario <= 0:
            raise ValueError("Valor unitário deve ser maior que zero")

        produto_model = ProdutoModel(
            descricao=request.descricao,
            valor_unitario=request.valor_unitario,
            img_url=request.img_url
        )

        await self.produto_dao.criar_novo_produto(produto_model, id_usuario_logado)

        return NovoProdutoResponse(
            descricao=request.descricao,
            valor_unitario=request.valor_unitario,
            img_url=request.img_url
        ).to_dict()