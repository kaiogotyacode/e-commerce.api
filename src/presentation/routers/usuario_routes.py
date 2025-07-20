# src/presentation/routers/usuario_routes.py
from fastapi import APIRouter, Depends
from domain.dependencies.usuario_bearer_token_dependency import validar_token_usuario
from presentation.controllers.usuario_controller import UsuarioController
from application.dto.usuario.request.novo_usuario_request import NovoUsuarioRequest

router = APIRouter(
    prefix="/usuario",
    tags=["Usuários"]
)

usuario_controller = UsuarioController()

@router.post("/novo_usuario", response_model=None)
async def criar_novo_usuario(request: NovoUsuarioRequest):
    """
    Criar um novo usuário no sistema.
    
    - **nome**: Nome completo do usuário
    - **email**: Email válido e único
    - **senha**: Senha do usuário
    """
    return await usuario_controller.criar_usuario(request)

@router.post("/listar_usuarios", dependencies=[Depends(validar_token_usuario)], response_model=None)
async def listar_usuarios():
    """
    Listar todos os usuários do sistema.
    """
    return await usuario_controller.listar_usuarios()