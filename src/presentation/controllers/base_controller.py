# src/presentation/controllers/base_controller.py
from abc import ABC

class BaseController(ABC):
    """
    Classe base para todos os controllers.
    Fornece funcionalidades comuns para manipulação de requisições HTTP.
    """
    
    def __init__(self):
        pass
    
    def _handle_error(self, error: Exception, default_message: str = "Erro interno"):
        """
        Método helper para tratamento de erros comuns
        """
        # Aqui você pode adicionar logging, formatação de erro, etc.
        return {
            "error": True,
            "message": str(error) if str(error) else default_message
        }
    
    def _success_response(self, content: any = None, message: str = "Sucesso"):
        """
        Método helper para respostas de sucesso padronizadas
        """
        return {
            "error": False,
            "message": message,
            "content": content
        }