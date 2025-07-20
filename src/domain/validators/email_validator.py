"""
Validador de email robusto
Suporta múltiplas abordagens de validação
"""
import re
from typing import Tuple
from email_validator import validate_email, EmailNotValidError

class EmailValidator:
    """Classe para validação robusta de emails"""
    
    # Regex mais rigoroso para validação de email
    EMAIL_REGEX = re.compile(
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )
    
    # Lista de domínios suspeitos/temporários (básica)
    BLOCKED_DOMAINS = {
        '10minutemail.com', 'tempmail.org', 'guerrillamail.com',
        'mailinator.com', 'temp-mail.org', 'throwaway.email'
    }
    
    @classmethod
    def validate_email_comprehensive(cls, email: str) -> Tuple[bool, str]:
        """
        Validação compreensiva de email
        
        Returns:
            Tuple[bool, str]: (is_valid, error_message)
        """
        if not email:
            return False, "Email é obrigatório"
        
        # 1. Validação básica de formato
        if not cls._basic_validation(email):
            return False, "Formato de email inválido"
        
        # 2. Validação com biblioteca especializada
        try:
            validated_email = validate_email(email)
            normalized_email = validated_email.email
        except EmailNotValidError as e:
            return False, f"Email inválido: {str(e)}"
        
        # 3. Verificação de domínio bloqueado
        domain = email.split('@')[1].lower()
        if domain in cls.BLOCKED_DOMAINS:
            return False, "Domínio de email não permitido"
        
        # 4. Verificações adicionais
        if not cls._additional_checks(email):
            return False, "Email não atende aos critérios de segurança"
        
        return True, normalized_email
    
    @classmethod
    def _basic_validation(cls, email: str) -> bool:
        """Validação básica com regex"""
        return bool(cls.EMAIL_REGEX.match(email))
    
    @classmethod
    def _additional_checks(cls, email: str) -> bool:
        """Verificações adicionais de segurança"""
        # Não pode começar ou terminar com ponto
        local_part = email.split('@')[0]
        if local_part.startswith('.') or local_part.endswith('.'):
            return False
        
        # Não pode ter pontos consecutivos
        if '..' in email:
            return False
        
        # Tamanho razoável
        if len(email) > 254:  # RFC 5321
            return False
        
        if len(local_part) > 64:  # RFC 5321
            return False
        
        return True
    
    @classmethod
    def validate_email_simple(cls, email: str) -> Tuple[bool, str]:
        """Validação simples para casos menos rigorosos"""
        if not email or '@' not in email:
            return False, "Email inválido"
        
        if not cls._basic_validation(email):
            return False, "Formato de email inválido"
        
        return True, email.lower().strip()
    
    @classmethod
    def normalize_email(cls, email: str) -> str:
        """Normaliza o email (remove espaços, converte para minúsculo)"""
        if not email:
            return ""
        
        return email.lower().strip()
