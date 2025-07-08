# Estrutura DAO com BaseDAO

## Visão Geral

Foi implementada uma estrutura de DAO (Data Access Object) com uma classe base `BaseDAO` que fornece operações CRUD padrão para todas as tabelas do banco de dados.

## Estrutura Implementada

### BaseDAO (`src/infrastructure/dao/postgres/common/base_dao.py`)

Classe abstrata que fornece:

- **Métodos CRUD padrão**:
  - `criar(model)` - Inserir novo registro
  - `buscar_por_id(id_value)` - Buscar por ID
  - `buscar_todos()` - Buscar todos os registros
  - `atualizar(id_value, model)` - Atualizar registro existente
  - `deletar(id_value)` - Deletar registro
  - `buscar_por_filtro(**kwargs)` - Buscar com filtros personalizados

- **Propriedades abstratas obrigatórias**:
  - `table_name` - Nome da tabela no banco
  - `model_class` - Classe do modelo de dados
  - `primary_key_field` - Nome do campo chave primária

### UsuarioDAO Atualizado

O `UsuarioDAO` foi refatorado para:
- Herdar de `BaseDAO`
- Implementar as propriedades abstratas obrigatórias
- Manter o método `criar_novo_usuario()` para compatibilidade
- Adicionar métodos específicos como `buscar_por_email()`

### UsuarioModel Atualizado

Adicionado campo `id: Optional[int] = None` para suportar operações CRUD completas.

## Como Usar

### Exemplo Básico - UsuarioDAO

```python
from src.infrastructure.dao.postgres.usuario.usuario_dao import UsuarioDAO
from src.domain.models.usuario.usuario_model import UsuarioModel

# Instanciar DAO
dao = UsuarioDAO()

# Criar usuário
usuario = UsuarioModel(nome="João", email="joao@test.com", senha="123")
await dao.criar(usuario)

# Buscar todos
usuarios = await dao.buscar_todos()

# Buscar por ID
usuario = await dao.buscar_por_id(1)

# Atualizar
await dao.atualizar(1, usuario_atualizado)

# Deletar
await dao.deletar(1)

# Buscar com filtros
usuarios = await dao.buscar_por_filtro(email="joao@test.com")

# Métodos específicos
usuario = await dao.buscar_por_email("joao@test.com")
```

### Como Criar Novos DAOs

1. **Crie o modelo de dados** (dataclass)
2. **Crie a classe DAO** herdando de `BaseDAO`
3. **Implemente as propriedades abstratas**
4. **Adicione métodos específicos** se necessário

Exemplo para uma tabela de produtos:

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
        return "id"
    
    # Métodos específicos
    async def buscar_por_categoria(self, categoria_id: int):
        return await self.buscar_por_filtro(categoria_id=categoria_id)
```

## Vantagens da Estrutura

1. **Reutilização de código** - Operações CRUD padrão são herdadas
2. **Consistência** - Todas as DAOs seguem o mesmo padrão
3. **Manutenibilidade** - Mudanças na BaseDAO afetam todas as DAOs
4. **Flexibilidade** - Cada DAO pode ter métodos específicos
5. **Type Safety** - Uso de tipos para melhor IDE support

## Arquivos Criados/Modificados

- ✅ `src/infrastructure/dao/postgres/common/base_dao.py` - Classe base
- ✅ `src/infrastructure/dao/postgres/usuario/usuario_dao.py` - DAO atualizado
- ✅ `src/domain/models/usuario/usuario_model.py` - Modelo atualizado
- ✅ `src/infrastructure/dao/postgres/template_dao.py` - Template para novos DAOs
- ✅ `exemplo_uso_dao.py` - Exemplo de uso

## Próximos Passos

1. Teste a implementação com sua base de dados
2. Ajuste o campo `primary_key_field` se necessário
3. Crie novos DAOs usando o template fornecido
4. Considere adicionar validações específicas na BaseDAO se necessário
