from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from typing import Optional

security = HTTPBearer()
SECRET_KEY = 'Ec0MDoj4pA$3g!7tWz9R&f#LuKmQ2pSxN'

def validar_token_usuario(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Verifica se o token Bearer é válido
    """
    try:
        token = credentials.credentials
        # Aqui você deve implementar a lógica de validação do seu token
        # Por exemplo, decodificar JWT, verificar com banco de dados, etc.
        
        # Exemplo básico de validação JWT (substitua pela sua lógica)
        payload = jwt.decode(token, SECRET_KEY , algorithms=["HS256"])
        
        # Se chegou até aqui, o token é válido
        return token
        
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expirado"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido"
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Não autorizado"
        )