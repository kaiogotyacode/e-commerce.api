from application.dto.base_dto import BaseDTO

class VincularProdutoExibicaoRequest(BaseDTO):
    id_produto: int = None
    id_exibicao: int = None
    order_list: int = None
