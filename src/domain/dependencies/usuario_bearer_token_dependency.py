from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

security = HTTPBearer()
SECRET_KEY = 'Ec0MDoj4pA$3g!7tWz9R&f#LuKmQ2pSxN'

def validar_token_usuario(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Verifica se o token Bearer é válido
    """
    try:
        token = credentials.credentials
        payload : dict = jwt.decode(token, SECRET_KEY , algorithms=["HS256"])

        return payload.get('user_id', None)
        
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