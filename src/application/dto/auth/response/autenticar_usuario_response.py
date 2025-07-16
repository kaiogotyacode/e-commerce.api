from application.dto.base_dto import BaseDTO

class AutenticarUsuarioResponse(BaseDTO):
    mensagem: str
    token: str = None