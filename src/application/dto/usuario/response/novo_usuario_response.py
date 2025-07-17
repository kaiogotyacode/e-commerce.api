from application.dto.base_dto import BaseDTO

class NovoUsuarioResponse(BaseDTO):
    email : str = None
    nome : str = None