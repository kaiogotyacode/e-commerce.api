from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class BaseModel:
    """
    Classe base para todos os modelos que integram com a base de dados.
    Contém campos padrão de auditoria e controle.
    
    Nota: A chave primária específica (id_usuario, id_pedido, etc.) 
    deve ser definida em cada modelo filho.
    """
    
    # Campos de auditoria - inclusão
    u_inclusao: Optional[int] = None  # ID do usuário que incluiu o registro
    inclusao: Optional[datetime] = None  # Data/hora da inclusão
    
    # Campos de auditoria - alteração
    u_alteracao: Optional[int] = None  # ID do usuário que fez a última alteração
    alteracao: Optional[datetime] = None  # Data/hora da última alteração
    
    def marcar_inclusao(self, usuario_id: int) -> None:
        """
        Marca o registro como incluído pelo usuário especificado.
        Define u_inclusao e inclusao com a data/hora atual.
        """
        self.u_inclusao = usuario_id
        self.inclusao = datetime.now()
    
    def marcar_alteracao(self, usuario_id: int) -> None:
        """
        Marca o registro como alterado pelo usuário especificado.
        Define u_alteracao e alteracao com a data/hora atual.
        """
        self.u_alteracao = usuario_id
        self.alteracao = datetime.now()
    
    def get_primary_key_value(self, primary_key_field: str) -> Optional[int]:
        """
        Obtém o valor da chave primária baseado no nome do campo.
        
        Args:
            primary_key_field: Nome do campo da chave primária (ex: 'id_usuario', 'id_pedido')
            
        Returns:
            Valor da chave primária ou None se não existir
        """
        return getattr(self, primary_key_field, None)
    
    def set_primary_key_value(self, primary_key_field: str, value: Optional[int]) -> None:
        """
        Define o valor da chave primária baseado no nome do campo.
        
        Args:
            primary_key_field: Nome do campo da chave primária
            value: Valor a ser definido
        """
        setattr(self, primary_key_field, value)
    
    def is_novo_registro(self, primary_key_field: str) -> bool:
        """
        Verifica se é um novo registro (sem chave primária definida).
        
        Args:
            primary_key_field: Nome do campo da chave primária
            
        Returns:
            True se é um novo registro, False caso contrário
        """
        pk_value = self.get_primary_key_value(primary_key_field)
        return pk_value is None
    
    def preparar_para_inclusao(self, usuario_id: int) -> None:
        """
        Prepara o modelo para inclusão no banco de dados.
        Marca a inclusão com o usuário responsável.
        
        Nota: A chave primária deve permanecer None para ser auto-gerada
        """
        self.marcar_inclusao(usuario_id)
    
    def preparar_para_alteracao(self, usuario_id: int) -> None:
        """
        Prepara o modelo para alteração no banco de dados.
        Marca a alteração com o usuário responsável.
        """
        self.marcar_alteracao(usuario_id)