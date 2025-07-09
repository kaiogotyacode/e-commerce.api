# Estrutura DAO com BaseDAO e BaseModel

## Visão Geral

Foi implementada uma estrutura completa de DAO (Data Access Object) e Model com:
- **BaseDAO**: Classe base que fornece operações CRUD padrão
- **BaseModel**: Classe base com campos de auditoria padrão (id, u_inclusao, inclusao, u_alteracao, alteracao)

## Estrutura Implementada

### BaseModel (`src/domain/models/common/base_model.py`)

Classe base para todos os modelos com campos de auditoria:

- **Campos padrão**:
  - `id: Optional[int]` - Chave primária
  - `u_inclusao: Optional[int]` - ID do usuário que incluiu
  - `inclusao: Optional[datetime]` - Data/hora da inclusão
  - `u_alteracao: Optional[int]` - ID do usuário que alterou
  - `alteracao: Optional[datetime]` - Data/hora da última alteração

- **Métodos úteis**:
  - `marcar_inclusao(usuario_id)` - Marca campos de inclusão
  - `marcar_alteracao(usuario_id)` - Marca campos de alteração
  - `is_novo_registro()` - Verifica se é novo registro
  - `preparar_para_inclusao(usuario_id)` - Prepara para insert
  - `preparar_para_alteracao(usuario_id)` - Prepara para update

### BaseDAO (`src/infrastructure/dao/postgres/common/base_dao.py`)

Classe abstrata que fornece:

- **Métodos CRUD com auditoria**:
  - `criar(model, usuario_id=None)` - Inserir com auditoria opcional
  - `buscar_por_id(id_value)` - Buscar por ID
  - `buscar_todos()` - Buscar todos os registros
  - `atualizar(id_value, model, usuario_id=None)` - Atualizar com auditoria opcional
  - `deletar(id_value)` - Deletar registro
  - `buscar_por_filtro(**kwargs)` - Buscar com filtros personalizados

- **Propriedades abstratas obrigatórias**:
  - `table_name` - Nome da tabela no banco
  - `model_class` - Classe do modelo de dados
  - `primary_key_field` - Nome do campo chave primária

### UsuarioDAO e UsuarioModel Atualizados

- **UsuarioModel** agora herda de `BaseModel` 
- **Campos de auditoria** incluídos automaticamente
- **UsuarioDAO** atualizado para usar campos padrão (`id` ao invés de `id_usuario`)
- **Métodos com auditoria** disponíveis

## Como Usar

### Exemplo com Auditoria

```python
from src.infrastructure.dao.postgres.usuario.usuario_dao import UsuarioDAO
from src.domain.models.usuario.usuario_model import UsuarioModel

# Instanciar DAO
dao = UsuarioDAO()
usuario_logado_id = 1  # ID do usuário que está fazendo a operação

# Criar usuário com auditoria
usuario = UsuarioModel(nome="João", email="joao@test.com", senha="123")
await dao.criar(usuario, usuario_id=usuario_logado_id)

# Buscar todos
usuarios = await dao.buscar_todos()

# Buscar por ID
usuario = await dao.buscar_por_id(1)

# Atualizar com auditoria
usuario.nome = "João Atualizado"
await dao.atualizar(1, usuario, usuario_id=usuario_logado_id)

# Deletar
await dao.deletar(1)

# Métodos específicos de auditoria
print(f"Incluído por: {usuario.u_inclusao}")
print(f"Data inclusão: {usuario.inclusao}")
print(f"Alterado por: {usuario.u_alteracao}")
print(f"Data alteração: {usuario.alteracao}")
```

### Como Criar Novos Models e DAOs

1. **Crie o modelo herdando de BaseModel**:

```python
from dataclasses import dataclass
from domain.models.common.base_model import BaseModel

@dataclass
class ProdutoModel(BaseModel):
    nome: str
    preco: float
    categoria_id: int
    # Herda automaticamente: id, u_inclusao, inclusao, u_alteracao, alteracao
```

2. **Crie o DAO herdando de BaseDAO**:

```python
from infrastructure.dao.postgres.common.base_dao import BaseDAO
from domain.models.produto.produto_model import ProdutoModel

class ProdutoDAO(BaseDAO):
    @property
    def table_name(self) -> str:
        return "loja.tbl_produto"
    
    @property
    def model_class(self):
        return ProdutoModel
    
    @property
    def primary_key_field(self) -> str:
        return "id"  # Campo padrão do BaseModel
    
    # Métodos específicos com auditoria
    async def criar_produto_com_auditoria(self, produto: ProdutoModel, usuario_id: int):
        await self.criar(produto, usuario_id=usuario_id)
```

3. **Crie a estrutura SQL correspondente**:

```sql
CREATE TABLE loja.tbl_produto (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    categoria_id INTEGER NOT NULL,
    
    -- Campos de auditoria padrão
    u_inclusao INTEGER,
    inclusao TIMESTAMP DEFAULT NOW(),
    u_alteracao INTEGER,
    alteracao TIMESTAMP
);
```

## Vantagens da Nova Estrutura

1. **Auditoria automática** - Rastreamento completo de inclusões e alterações
2. **Reutilização de código** - Operações CRUD padrão são herdadas
3. **Consistência** - Todas as tabelas seguem o mesmo padrão de auditoria
4. **Manutenibilidade** - Mudanças na BaseDAO/BaseModel afetam todo o sistema
5. **Flexibilidade** - Cada DAO pode ter métodos específicos
6. **Type Safety** - Uso de tipos para melhor IDE support
7. **Rastreabilidade** - Saber quem e quando fez cada operação

## Arquivos Criados/Modificados

- ✅ `src/domain/models/common/base_model.py` - **NOVO** - Classe base para modelos
- ✅ `src/infrastructure/dao/postgres/common/base_dao.py` - Classe base para DAOs
- ✅ `src/infrastructure/dao/postgres/usuario/usuario_dao.py` - DAO atualizado
- ✅ `src/domain/models/usuario/usuario_model.py` - Modelo com herança
- ✅ `src/infrastructure/dao/postgres/template_dao.py` - Template atualizado
- ✅ `exemplo_uso_auditoria.py` - **NOVO** - Exemplo com auditoria
- ✅ `database_structure.sql` - **NOVO** - Scripts SQL para tabelas

## Próximos Passos

1. **Execute os scripts SQL** para criar as tabelas com campos de auditoria
2. **Teste a implementação** com sua base de dados
3. **Migre modelos existentes** para herdar de `BaseModel`
4. **Crie novos DAOs** usando o template fornecido
5. **Implemente auditoria** nas operações críticas passando `usuario_id`
6. **Configure triggers SQL** (opcional) para auditoria automática
