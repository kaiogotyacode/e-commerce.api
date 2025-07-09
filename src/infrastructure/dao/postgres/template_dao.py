# Template para criar novos DAOs herdando de BaseDAO

"""
TEMPLATE PARA NOVOS DAOS COM BASEMODEL

Para criar um novo DAO, siga este template:

1. Crie o modelo herdando de BaseModel
2. Importe BaseDAO e o modelo correspondente
3. Herde de BaseDAO
4. Implemente as propriedades abstratas obrigatórias
5. Adicione métodos específicos se necessário

Exemplo para uma tabela "produto":
"""

# 1. PRIMEIRO CRIE O MODELO (exemplo: produto_model.py)
from dataclasses import dataclass
from domain.models.common.base_model import BaseModel

@dataclass
class ProdutoModel(BaseModel):
    nome: str
    preco: float
    categoria_id: int
    # Herda automaticamente de BaseModel:
    # id, u_inclusao, inclusao, u_alteracao, alteracao

# 2. DEPOIS CRIE O DAO
from infrastructure.dao.postgres.common.base_dao import BaseDAO
# from domain.models.produto.produto_model import ProdutoModel  # Substitua pelo seu modelo

class ProdutoDAO(BaseDAO):
    """
    DAO para a tabela de produtos
    """
    
    @property
    def table_name(self) -> str:
        """Nome da tabela no banco de dados"""
        return "loja.tbl_produto"  # Ajuste o schema e nome da tabela
    
    @property
    def model_class(self):
        """Classe do modelo associado ao DAO"""
        # return ProdutoModel  # Substitua pela sua classe de modelo
        pass
    
    @property
    def primary_key_field(self) -> str:
        """Nome do campo chave primária"""
        return "id"  # Campo padrão do BaseModel
    
    # Métodos específicos para ProdutoDAO (opcionais)
    async def buscar_por_categoria(self, categoria_id: int):
        """Exemplo de método específico"""
        return await self.buscar_por_filtro(categoria_id=categoria_id)
    
    async def criar_produto_com_auditoria(self, produto: 'ProdutoModel', usuario_id: int):
        """Método específico para criar produto com auditoria"""
        await self.criar(produto, usuario_id=usuario_id)
    
    async def atualizar_produto_com_auditoria(self, produto_id: int, produto: 'ProdutoModel', usuario_id: int):
        """Método específico para atualizar produto com auditoria"""
        return await self.atualizar(produto_id, produto, usuario_id=usuario_id)

"""
CAMPOS HERDADOS DO BASEMODEL:

Todos os modelos que herdam de BaseModel automaticamente têm:

1. id: Optional[int] = None - Chave primária
2. u_inclusao: Optional[int] = None - ID do usuário que incluiu
3. inclusao: Optional[datetime] = None - Data/hora da inclusão
4. u_alteracao: Optional[int] = None - ID do usuário que alterou
5. alteracao: Optional[datetime] = None - Data/hora da última alteração

MÉTODOS DISPONÍVEIS NO BASEMODEL:

1. marcar_inclusao(usuario_id) - Marca inclusão
2. marcar_alteracao(usuario_id) - Marca alteração
3. is_novo_registro() - Verifica se é novo
4. preparar_para_inclusao(usuario_id) - Prepara para insert
5. preparar_para_alteracao(usuario_id) - Prepara para update

MÉTODOS ATUALIZADOS NA BASEDAO:

1. criar(model, usuario_id=None) - Com auditoria opcional
2. atualizar(id_value, model, usuario_id=None) - Com auditoria opcional
3. Outros métodos mantêm a mesma assinatura

ESTRUTURA SQL RECOMENDADA:

CREATE TABLE schema.tbl_exemplo (
    id SERIAL PRIMARY KEY,
    -- seus campos específicos aqui --
    nome VARCHAR(255),
    
    -- campos de auditoria --
    u_inclusao INTEGER,
    inclusao TIMESTAMP,
    u_alteracao INTEGER,
    alteracao TIMESTAMP
);
"""
