import jwt
from datetime import datetime, timedelta
from typing import Dict, Any
import os

class JWTManager:
    def __init__(self):
        self.secret_key = os.getenv('JWT_SECRET_KEY', 'Ec0MDoj4pA$3g!7tWz9R&f#LuKmQ2pSxN')
        self.algorithm = 'HS256'
        self.expiration_hours = 24

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