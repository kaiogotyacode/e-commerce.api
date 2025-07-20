from application.dto.exibicao_produto.request.vincular_produto_exibicao_request import VincularProdutoExibicaoRequest
from application.dto.produto.request.novo_produto_request import NovoProdutoRequest
from application.dto.produto.response.novo_produto_response import NovoProdutoResponse
from domain.exceptions.conflict_exception import ConflictException
from domain.exceptions.unauthorized_exception import UnauthorizedException
from domain.models.exibicao_produto.exibicao_produto_model import ExibicaoProdutoModel
from domain.models.produto.produto_model import ProdutoModel
from domain.models.usuario.usuario_model import UsuarioModel
from infrastructure.dao.postgres.exibicao_produto.exibicao_produto_dao import ExibicaoProdutoDAO
from infrastructure.dao.postgres.usuario.usuario_dao import UsuarioDAO


class ExibicaoProdutoBO:
    def __init__(self):
        self.exibicao_produto_dao = ExibicaoProdutoDAO()
        self.usuario_dao = UsuarioDAO()
        
    async def vincular_produto_exibicao(self, request : VincularProdutoExibicaoRequest, id_usuario_logado : int):
        usuario_logado : UsuarioModel = await self.usuario_dao.buscar_por_id(id_usuario_logado)
        
        if not usuario_logado.admin:
            raise UnauthorizedException("Usuário não autorizado.")
        
        exibicao_produto = await self.exibicao_produto_dao.validar_existencia_produto_exibicao(
            id_exibicao=request.id_exibicao,
            id_produto=request.id_produto
        )

        if exibicao_produto:
            raise ConflictException("Produto já vinculado a esta exibição.")
        
        exibicao_produto_model = ExibicaoProdutoModel(
            id_exibicao=request.id_exibicao,
            id_produto=request.id_produto,
            order_list=request.order_list
        )
    
        await self.exibicao_produto_dao.criar_vinculo_exibicao_produto(exibicao_produto_model, id_usuario_logado)