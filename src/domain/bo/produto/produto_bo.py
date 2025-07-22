from typing import List
import bcrypt
from application.dto.produto.request.novo_produto_request import NovoProdutoRequest
from application.dto.produto.response.novo_produto_response import NovoProdutoResponse
from domain.exceptions.unauthorized_exception import UnauthorizedException
from domain.models.produto.produto_model import ProdutoModel
from domain.models.usuario.usuario_model import UsuarioModel
from infrastructure.dao.postgres.produto.produto_dao import ProdutoDAO
from infrastructure.dao.postgres.usuario.usuario_dao import UsuarioDAO


class ProdutoBO:
    def __init__(self):
        self.produto_dao = ProdutoDAO()
        self.usuario_dao = UsuarioDAO()

    async def novo_produto(self, request : NovoProdutoRequest, id_usuario_logado : int) -> NovoProdutoResponse:
        usuario_logado : UsuarioModel = await self.usuario_dao.buscar_por_id(id_usuario_logado)

        if not usuario_logado.admin:
            raise UnauthorizedException("Usuário não autorizado a cadastrar produtos.")

        if not request.descricao or len(request.descricao) < 10:
            raise ValueError("Descrição deve ter pelo menos 10 caracteres")

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

    async def listar_produtos_por_tela(self, request: ListarProdutosTelaRequest) -> ListarProdutosTelaResponse:
        # Se a tela for Home:

            # Exibicao: { exibicao_1st | exibicao_2nd } 
            # Banner: {
            # Carrousel: { carrousel_1st },
            # BannerDefault: { banner_1st, banner_2nd },
            # FullWidth: { full_width_1st }
            # }
         
        #  produtos = await self.produto_dao.listar_produtos_por_tela(request)

        # validações

        pass

    async def listar_produtos_home(self):
        pass

    async def listar_produtos_lancamentos(self):
        pass

    async def exibir_produto_detalhe(self):
        # Definir padrão visual da tela de Detalhe do Produto
        # Nos campos de Exibição e Banner, as imagens devem estar relacionadas ao TIPO DO PRODUTO (add nova propriedade).
        pass
    