# src/presentation/controllers/base_controller.py
from abc import ABC
from functools import wraps
from fastapi import HTTPException, status
from domain.exceptions.unauthorized_exception import UnauthorizedException
from domain.exceptions.bad_request_exception import BadRequestException
from domain.exceptions.forbidden_exception import ForbiddenException
from domain.exceptions.not_found_exception import NotFoundException
from domain.exceptions.conflict_exception import ConflictException

def handle_exceptions(func):
    """
    Decorator para tratamento automático de exceções.
    Uso: @handle_exceptions
    """
    @wraps(func)
    async def wrapper(self, *args, **kwargs):
        try:
            return await func(self, *args, **kwargs)
        except Exception as e:
            self._handle_business_exceptions(e)
    return wrapper

class BaseController(ABC):
    """
    Classe base para todos os controllers.
    Fornece funcionalidades comuns para manipulação de requisições HTTP.
    """
    
    def __init__(self):
        pass
    
    def _handle_business_exceptions(self, error: Exception):
        """
        Método centralizado para tratamento de exceções de negócio.
        Converte exceções customizadas em HTTPException com status code apropriado.
        """
        if isinstance(error, UnauthorizedException):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=str(error)
            )
        elif isinstance(error, ForbiddenException):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=str(error)
            )
        elif isinstance(error, BadRequestException):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(error)
            )
        elif isinstance(error, NotFoundException):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(error)
            )
        elif isinstance(error, ConflictException):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=str(error)
            )
        elif isinstance(error, ValueError):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(error)
            )
        else:
            # Para exceções não mapeadas, retorna erro 500
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=self._handle_error(error, "Erro interno do servidor")
            )
    
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