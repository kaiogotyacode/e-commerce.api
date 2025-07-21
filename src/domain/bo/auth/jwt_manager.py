import jwt
from datetime import datetime, timedelta
from typing import Annotated, Dict, Any
import os

class JWTManager:
    def __init__(self):
        self.secret_key = os.getenv('JWT_SECRET_KEY', 'ChaveAleatoria-E-commerce$u7#Xf!9wVz@3LpTgQm2')
        self.algorithm = os.getenv('JWT_ALGORITHM')
        self.expiration_hours = int(os.getenv('JWT_EXPIRATION_HOURS'))

    def generate_token(self, user_id: int) -> str:
        """Gera um token JWT para o usuário"""
        payload = {
            'user_id': user_id,
            'exp': datetime.now() + timedelta(hours=self.expiration_hours),
            'iat': datetime.now()
        }
        
        token = jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
        return token

    def verify_token(self, token: str) -> Dict[str, Any]:
        """Verifica e decodifica um token JWT"""
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            raise ValueError("Token expirado")
        except jwt.InvalidTokenError:
            raise ValueError("Token inválido")
