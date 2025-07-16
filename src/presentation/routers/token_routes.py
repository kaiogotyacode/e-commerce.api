from fastapi import APIRouter
from application.dto.auth.request.autenticar_usuario_request import AutenticarUsuarioRequest
from presentation.controllers.token_controller import TokenController

router = APIRouter(
    prefix="/token",
    tags=["Token"]
)

token_controller = TokenController()

@router.post("/autenticar_usuario", response_model=None)
async def autenticar_usuario(request: AutenticarUsuarioRequest):
    return await token_controller.autenticar_usuario(request)