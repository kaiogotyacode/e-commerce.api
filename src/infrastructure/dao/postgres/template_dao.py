# Template para criar novos DAOs herdando de BaseDAO

"""
TEMPLATE PARA NOVOS DAOS

Para criar um novo DAO, siga este template:

1. Importe BaseDAO e o modelo correspondente
2. Herde de BaseDAO
3. Implemente as propriedades abstratas obrigatórias
4. Adicione métodos específicos se necessário

Exemplo para uma tabela "produto":
"""

from infrastructure.dao.postgres.common.base_dao import BaseDAO
# from domain.models.produto.produto_model import ProdutoModel  # Substitua pelo seu modelo

class ProdutoDAO(BaseDAO):
    """
    DAO para a tabela de produtos
    """
    
    @property
    def table_name(self) -> str:
        """Nome da tabela no banco de dados"""
        return "schema.tbl_produto"  # Ajuste o schema e nome da tabela
    
    @property
    def model_class(self):
        """Classe do modelo associado ao DAO"""
        # return ProdutoModel  # Substitua pela sua classe de modelo
        pass
    
    @property
    def primary_key_field(self) -> str:
        """Nome do campo chave primária"""
        return "id"  # Ajuste se necessário
    
    # Métodos específicos para ProdutoDAO (opcionais)
    async def buscar_por_categoria(self, categoria_id: int):
        """Exemplo de método específico"""
        return await self.buscar_por_filtro(categoria_id=categoria_id)
    
    async def buscar_por_preco_range(self, preco_min: float, preco_max: float):
        """Exemplo de busca com condições mais complexas"""
        conn = await self._get_connection()
        try:
            query = f"""
                SELECT * FROM {self.table_name} 
                WHERE preco BETWEEN $1 AND $2
            """
            rows = await conn.fetch(query, preco_min, preco_max)
            return [self._dict_to_model(dict(row)) for row in rows]
        finally:
            await conn.close()

"""
MÉTODOS DISPONÍVEIS NA BaseDAO:

Todos os DAOs que herdam de BaseDAO automaticamente têm acesso a:

1. criar(model) - Insere um novo registro
2. buscar_por_id(id_value) - Busca por ID
3. buscar_todos() - Retorna todos os registros
4. atualizar(id_value, model) - Atualiza um registro
5. deletar(id_value) - Deleta um registro
6. buscar_por_filtro(**kwargs) - Busca com filtros personalizados

IMPORTANTE:
- Certifique-se de que seu modelo seja um dataclass
- O campo da chave primária deve existir na tabela
- Para campos opcionais (como ID), use Optional[tipo] no modelo
"""
