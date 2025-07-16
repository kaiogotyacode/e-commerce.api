from application.dto.base_dto import BaseDTO

class AutenticarUsuarioRequest(BaseDTO):
    email : str
    senha : str