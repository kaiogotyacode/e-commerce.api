from abc import ABC, abstractmethod
from typing import List, Optional, Any, Dict
import asyncpg
from dataclasses import dataclass, fields

class BaseDAO(ABC):
    """
    Classe base para todos os DAOs com operações CRUD padrão.
    """
    
    def __init__(self):
        self.dsn = "postgresql://neondb_owner:npg_Xpi4jSxqdM3R@ep-ancient-glade-a87hrwfe-pooler.eastus2.azure.neon.tech/neondb?sslmode=require&channel_binding=require"
    
    @property
    @abstractmethod
    def table_name(self) -> str:
        """Nome da tabela no banco de dados"""
        pass
    
    @property
    @abstractmethod
    def model_class(self):
        """Classe do modelo associado ao DAO"""
        pass
    
    @property
    @abstractmethod
    def primary_key_field(self) -> str:
        """Nome do campo chave primária"""
        pass
    
    async def _get_connection(self) -> asyncpg.Connection:
        """Obtém uma conexão com o banco de dados"""
        return await asyncpg.connect(dsn=self.dsn)
    
    def _model_to_dict(self, model: Any) -> Dict[str, Any]:
        """Converte um modelo dataclass para dicionário"""
        if hasattr(model, '__dataclass_fields__'):
            return {field.name: getattr(model, field.name) for field in fields(model)}
        else:
            return model.__dict__
    
    def _dict_to_model(self, data: Dict[str, Any]):
        """Converte um dicionário para o modelo"""
        return self.model_class(**data)
    
    async def criar(self, model: Any, usuario_id: int = None) -> None:
        """
        Insere um novo registro com ID automático (SERIAL/BIGSERIAL).
        O campo da chave primária será omitido para permitir auto-geração.
        
        Args:
            model: Modelo com os dados a serem inseridos
            usuario_id: ID do usuário para auditoria (opcional)
        """
        conn = await self._get_connection()
        try:
            # Prepara o modelo para inclusão se tiver o método
            if hasattr(model, 'preparar_para_inclusao') and usuario_id:
                model.preparar_para_inclusao(usuario_id)
            
            model_dict = self._model_to_dict(model)
            
            # ✅ SEMPRE remove o campo da chave primária para auto-geração
            if self.primary_key_field in model_dict:
                del model_dict[self.primary_key_field]
            
            if not model_dict:
                raise ValueError("Nenhum campo para inserir após remoção da chave primária")
            
            fields_names = list(model_dict.keys())
            fields_str = ', '.join(fields_names)
            placeholders = ', '.join([f'${i+1}' for i in range(len(fields_names))])
            values = [model_dict[field] for field in fields_names]
            
            query = f"INSERT INTO {self.table_name} ({fields_str}) VALUES ({placeholders})"
            await conn.execute(query, *values)
            
        finally:
            await conn.close()
    
    async def criar_com_id(self, model: Any, usuario_id: int = None) -> None:
        """
        Insere um novo registro com ID manual (fornecido no modelo).
        O campo da chave primária deve estar preenchido no modelo.
        
        Args:
            model: Modelo com os dados a serem inseridos (incluindo ID)
            usuario_id: ID do usuário para auditoria (opcional)
            
        Raises:
            ValueError: Se o ID não estiver definido no modelo
        """
        conn = await self._get_connection()
        try:
            # Prepara o modelo para inclusão se tiver o método
            if hasattr(model, 'preparar_para_inclusao') and usuario_id:
                model.preparar_para_inclusao(usuario_id)
            
            model_dict = self._model_to_dict(model)
            
            # ✅ Verifica se o ID foi fornecido
            pk_value = model_dict.get(self.primary_key_field)
            if pk_value is None:
                raise ValueError(f"Campo {self.primary_key_field} deve estar preenchido para inserção manual")
            
            fields_names = list(model_dict.keys())
            fields_str = ', '.join(fields_names)
            placeholders = ', '.join([f'${i+1}' for i in range(len(fields_names))])
            values = [model_dict[field] for field in fields_names]
            
            query = f"INSERT INTO {self.table_name} ({fields_str}) VALUES ({placeholders})"
            await conn.execute(query, *values)
            
        finally:
            await conn.close()
    
    async def criar_ou_atualizar(self, model: Any, usuario_id: int = None) -> str:
        """
        Inteligente: Cria se for novo registro ou atualiza se já existir.
        Verifica automaticamente baseado na presença da chave primária.
        
        Args:
            model: Modelo com os dados
            usuario_id: ID do usuário para auditoria (opcional)
            
        Returns:
            "CRIADO" ou "ATUALIZADO"
        """
        model_dict = self._model_to_dict(model)
        pk_value = model_dict.get(self.primary_key_field)
        
        if pk_value is None:
            # Novo registro - usar ID automático
            await self.criar(model, usuario_id)
            return "CRIADO"
        else:
            # Registro existente - atualizar
            await self.atualizar(pk_value, model, usuario_id)
            return "ATUALIZADO"

    async def buscar_por_id(self, id_value: Any) -> Optional[Any]:
        """Busca um registro pelo ID"""
        conn = await self._get_connection()
        try:
            query = f"SELECT * FROM {self.table_name} WHERE {self.primary_key_field} = $1"
            row = await conn.fetchrow(query, id_value)
            
            if row:
                return self._dict_to_model(dict(row))
            return None
            
        finally:
            await conn.close()
    
    async def buscar_todos(self) -> List[Any]:
        """Busca todos os registros da tabela"""
        conn = await self._get_connection()
        try:
            query = f"SELECT * FROM {self.table_name}"
            rows = await conn.fetch(query)
            
            return [self._dict_to_model(dict(row)) for row in rows]
            
        finally:
            await conn.close()
    
    async def atualizar(self, id_value: Any, model: Any, usuario_id: int = None) -> bool:
        """Atualiza um registro existente"""
        conn = await self._get_connection()
        try:
            # Prepara o modelo para alteração se tiver o método
            if hasattr(model, 'preparar_para_alteracao') and usuario_id:
                model.preparar_para_alteracao(usuario_id)
            
            model_dict = self._model_to_dict(model)
            # Remove o campo da chave primária se existir no modelo
            if self.primary_key_field in model_dict:
                del model_dict[self.primary_key_field]
            
            fields_names = list(model_dict.keys())
            set_clause = ', '.join([f'{field} = ${i+2}' for i, field in enumerate(fields_names)])
            values = [id_value] + [model_dict[field] for field in fields_names]
            
            query = f"UPDATE {self.table_name} SET {set_clause} WHERE {self.primary_key_field} = $1"
            result = await conn.execute(query, *values)
            
            # Verifica se alguma linha foi afetada
            return "UPDATE 1" in result
            
        finally:
            await conn.close()
    
    async def deletar(self, id_value: Any) -> bool:
        """Deleta um registro pelo ID"""
        conn = await self._get_connection()
        try:
            query = f"DELETE FROM {self.table_name} WHERE {self.primary_key_field} = $1"
            result = await conn.execute(query, id_value)
            
            # Verifica se alguma linha foi afetada
            return "DELETE 1" in result
            
        finally:
            await conn.close()
    
    async def buscar_por_filtro(self, **kwargs) -> List[Any]:
        """Busca registros com base em filtros específicos"""
        conn = await self._get_connection()
        try:
            if not kwargs:
                return await self.buscar_todos()
            
            conditions = []
            values = []
            param_count = 1
            
            for field, value in kwargs.items():
                conditions.append(f"{field} = ${param_count}")
                values.append(value)
                param_count += 1
            
            where_clause = " AND ".join(conditions)
            query = f"SELECT * FROM {self.table_name} WHERE {where_clause}"
            rows = await conn.fetch(query, *values)
            
            return [self._dict_to_model(dict(row)) for row in rows]
            
        finally:
            await conn.close()