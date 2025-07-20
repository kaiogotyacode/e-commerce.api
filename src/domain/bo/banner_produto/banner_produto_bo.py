from typing import List
import bcrypt
from application.dto.banner_produto.request.vincular_produto_banner_request import VincularProdutoBannerRequest
from domain.exceptions.conflict_exception import ConflictException
from domain.exceptions.unauthorized_exception import UnauthorizedException
from domain.models.banner_produto.exibicao_produto_model import BannerProdutoModel
from domain.models.usuario.usuario_model import UsuarioModel
from infrastructure.dao.postgres.banner_produto.banner_produto_dao import BannerProdutoDAO
from infrastructure.dao.postgres.usuario.usuario_dao import UsuarioDAO


class BannerProdutoBO:
    def __init__(self):
        self.banner_produto_dao = BannerProdutoDAO()
        self.usuario_dao = UsuarioDAO()
        
    async def vincular_produto_banner(self, request : VincularProdutoBannerRequest, id_usuario_logado : int):
        usuario_logado : UsuarioModel = await self.usuario_dao.buscar_por_id(id_usuario_logado)
        
        if not usuario_logado.admin:
            raise UnauthorizedException("Usuário não autorizado.")

        banner_produto = await self.banner_produto_dao.validar_existencia_banner_produto(
            id_tipo_banner=request.id_tipo_banner,
            id_produto=request.id_produto,
            id_tela=request.id_tela
        )

        if banner_produto:
            raise ConflictException("Produto já vinculado a este banner.")

        banner_produto_model = BannerProdutoModel(
            id_tipo_banner=request.id_tipo_banner,
            id_produto=request.id_produto,
            id_tela=request.id_tela,
            order_list=request.order_list
        )

        await self.banner_produto_dao.criar_vinculo_banner_produto(banner_produto_model, id_usuario_logado)