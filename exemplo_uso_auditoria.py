# Exemplo de uso com BaseModel e campos de auditoria

from src.infrastructure.dao.postgres.usuario.usuario_dao import UsuarioDAO
from src.domain.models.usuario.usuario_model import UsuarioModel
from datetime import datetime

async def exemplo_uso_com_auditoria():
    """
    Exemplo de como usar os novos campos de auditoria
    """
    dao = UsuarioDAO()
    
    # ID do usuário que está fazendo a operação (exemplo: usuário logado)
    usuario_logado_id = 1
    
    # === CRIAR NOVO USUÁRIO ===
    novo_usuario = UsuarioModel(
        nome="João Silva",
        email="joao@example.com",
        senha="senha123"
    )
    
    # Criar com auditoria automática
    await dao.criar(novo_usuario, usuario_id=usuario_logado_id)
    print("Usuário criado com auditoria!")
    print(f"Incluído por usuário ID: {novo_usuario.u_inclusao}")
    print(f"Data de inclusão: {novo_usuario.inclusao}")
    
    # === BUSCAR E ATUALIZAR ===
    # Buscar o usuário (assumindo que foi criado com ID = 2)
    usuario_existente = await dao.buscar_por_id(2)
    
    if usuario_existente:
        # Atualizar dados
        usuario_existente.nome = "João Silva Atualizado"
        usuario_existente.email = "joao.atualizado@example.com"
        
        # Atualizar com auditoria
        sucesso = await dao.atualizar(
            usuario_existente.id, 
            usuario_existente, 
            usuario_id=usuario_logado_id
        )
        
        if sucesso:
            print("Usuário atualizado com auditoria!")
            print(f"Alterado por usuário ID: {usuario_existente.u_alteracao}")
            print(f"Data de alteração: {usuario_existente.alteracao}")
    
    # === MÉTODOS ÚTEIS DO BASEMODEL ===
    outro_usuario = UsuarioModel(
        nome="Maria Santos",
        email="maria@example.com",
        senha="senha456"
    )
    
    # Verificar se é novo registro
    print(f"É novo registro? {outro_usuario.is_novo_registro()}")  # True
    
    # Preparar manualmente para inclusão
    outro_usuario.preparar_para_inclusao(usuario_logado_id)
    print(f"Preparado para inclusão por usuário: {outro_usuario.u_inclusao}")
    
    # Criar sem passar usuario_id (já foi marcado)
    await dao.criar(outro_usuario)

# === EXEMPLO DE HERANÇA PARA NOVO MODEL ===
from dataclasses import dataclass
from domain.models.common.base_model import BaseModel

@dataclass
class ProdutoModel(BaseModel):
    nome: str
    preco: float
    categoria_id: int
    # Herda automaticamente: id, u_inclusao, inclusao, u_alteracao, alteracao

# Para executar:
# import asyncio
# asyncio.run(exemplo_uso_com_auditoria())
