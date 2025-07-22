from fastapi import Depends
from application.dto.banner_produto.request.vincular_produto_banner_request import VincularProdutoBannerRequest
from application.dto.exibicao_produto.request.vincular_produto_exibicao_request import VincularProdutoExibicaoRequest
from application.dto.produto.request.novo_produto_request import NovoProdutoRequest
from domain.bo.banner_produto.banner_produto_bo import BannerProdutoBO
from domain.bo.exibicao_produto.exibicao_produto_bo import ExibicaoProdutoBO
from domain.bo.produto.produto_bo import ProdutoBO
from presentation.controllers.base_controller import BaseController, handle_exceptions
from domain.dependencies.usuario_bearer_token_dependency import validar_token_usuario

class ProdutoController(BaseController):
        
    def __init__(self):
        super().__init__()
        self.produto_bo = ProdutoBO()
        self.exibicao_produto_bo = ExibicaoProdutoBO()
        self.banner_produto_bo = BannerProdutoBO()

    @handle_exceptions
    async def cadastrar_novo_produto(self, request: NovoProdutoRequest, id_usuario_logado: int = Depends(validar_token_usuario)):
        resultado = await self.produto_bo.novo_produto(request, id_usuario_logado)
        return self._success_response(
            content=resultado,
            message="Produto criado com sucesso"
        )
    
    @handle_exceptions
    async def vincular_produto_exibicao(self, request: VincularProdutoExibicaoRequest, id_usuario_logado: int = Depends(validar_token_usuario)):
        await self.exibicao_produto_bo.vincular_produto_exibicao(request, id_usuario_logado)
        return self._success_response(
            content=None,
                message="Produto vinculado com sucesso"
            )
    
    @handle_exceptions
    async def vincular_produto_banner(self, request: VincularProdutoBannerRequest, id_usuario_logado: int = Depends(validar_token_usuario)):
        await self.banner_produto_bo.vincular_produto_banner(request, id_usuario_logado)
        return self._success_response(
            content=None,
                message="Produto vinculado com sucesso"
            )

    @handle_exceptions
    async def listar_produtos_por_tela(self, request: ListarProdutosTelaRequest):
        produtos = await self.produto_bo.listar_produtos_por_tela(request)
        return self._success_response(
            content=produtos,
            message="Produtos listados com sucesso"
        )