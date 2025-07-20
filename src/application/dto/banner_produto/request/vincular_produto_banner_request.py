from application.dto.base_dto import BaseDTO

class VincularProdutoBannerRequest(BaseDTO):
    id_produto: int = None
    id_tipo_banner: int = None
    id_tela: int = None
    order_list: int = None
