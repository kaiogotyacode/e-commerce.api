# src/presentation/routers/usuario_routes.py
from fastapi import APIRouter
from presentation.controllers.usuario_controller import UsuarioController
from application.dto.usuario.request.novo_usuario_request import NovoUsuarioRequest

# Criar o router com prefixo e tags
router = APIRouter(
    prefix="/usuario",
    tags=["Usuários"]  # Isso vai agrupar os endpoints na documentação
)

# Instanciar o controller
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