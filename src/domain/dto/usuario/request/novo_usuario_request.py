from pydantic import BaseModel

class NovoUsuarioRequest(BaseModel):
    nome : str
    email : str
    senha : str