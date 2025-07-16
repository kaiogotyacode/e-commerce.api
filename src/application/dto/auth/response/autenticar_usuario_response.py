from application.dto.base_dto import BaseDTO

class AutenticarUsuarioResponse(BaseDTO):
    token: str
    token_type: str
    expires_in: int