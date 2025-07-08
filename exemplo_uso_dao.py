# Exemplo de uso do UsuarioDAO com BaseDAO

from src.infrastructure.dao.postgres.usuario.usuario_dao import UsuarioDAO
from src.domain.models.usuario.usuario_model import UsuarioModel

async def exemplo_uso_usuario_dao():
    """
    Exemplo de como usar os métodos CRUD do UsuarioDAO
    """
    dao = UsuarioDAO()
    
    # Criar um novo usuário
    novo_usuario = UsuarioModel(
        nome="João Silva",
        email="joao@example.com",
        senha="senha123"
    )
    
    # Inserir no banco (usando método herdado da BaseDAO)
    await dao.criar(novo_usuario)
    print("Usuário criado com sucesso!")
    
    # Ou usar o método específico (mantém compatibilidade)
    await dao.criar_novo_usuario(novo_usuario)
    
    # Buscar todos os usuários
    todos_usuarios = await dao.buscar_todos()
    print(f"Total de usuários: {len(todos_usuarios)}")
    
    # Buscar usuário por ID (assumindo ID = 1)
    usuario = await dao.buscar_por_id(1)
    if usuario:
        print(f"Usuário encontrado: {usuario.nome}")
    
    # Buscar usuário por email (método específico)
    usuario_email = await dao.buscar_por_email("joao@example.com")
    if usuario_email:
        print(f"Usuário encontrado pelo email: {usuario_email.nome}")
    
    # Atualizar usuário
    if usuario:
        usuario_atualizado = UsuarioModel(
            nome="João Silva Atualizado",
            email="joao.novo@example.com",
            senha="nova_senha"
        )
        sucesso = await dao.atualizar(usuario.id, usuario_atualizado)
        if sucesso:
            print("Usuário atualizado com sucesso!")
    
    # Buscar com filtros personalizados
    usuarios_joao = await dao.buscar_por_filtro(nome="João Silva")
    print(f"Usuários com nome 'João Silva': {len(usuarios_joao)}")
    
    # Deletar usuário
    if usuario:
        sucesso = await dao.deletar(usuario.id)
        if sucesso:
            print("Usuário deletado com sucesso!")

# Para executar:
# import asyncio
# asyncio.run(exemplo_uso_usuario_dao())
