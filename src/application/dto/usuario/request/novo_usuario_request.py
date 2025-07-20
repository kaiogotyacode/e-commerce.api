from application.dto.base_dto import BaseDTO

class NovoUsuarioRequest(BaseDTO):
    nome : str
    email : str
    senha : str
    confirmar_senha : str