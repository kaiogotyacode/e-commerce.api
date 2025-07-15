# src/presentation/routers/usuario_routes.py
from fastapi import APIRouter
from presentation.controllers.pedido_controller import PedidoController
from application.dto.usuario.request.novo_usuario_request import NovoUsuarioRequest

# Criar o router com prefixo e tags
router = APIRouter(
    prefix="/pedido",
    tags=["Pedidos"]
)

pedido_controller = PedidoController()

@router.post("/novo_pedido", response_model=None)
async def criar_novo_pedido(request: NovoUsuarioRequest):
    """
    Criar um novo pedido em sistema.
    
    - **nome**: Nome completo do usuário
    - **email**: Email válido e único
    - **senha**: Senha do usuário
    """
    return await PedidoController.criar_pedido(request)