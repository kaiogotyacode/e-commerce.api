# import uvicorn
from fastapi import FastAPI

from domain.bo.usuario.usuario_bo import UsuarioBO
from application.dto.usuario.request.novo_usuario_request import NovoUsuarioRequest

# TODO: Aprender a como separar as "Tags" (Default) por Controllers, de forma individual/segregada.

app = FastAPI()


@app.get("/")
def home():
    return "API ON"

@app.get("/teste")
def teste():
    return "API ON - TESTE"

@app.post("/usuario/novo_usuario", response_model=None)
async def criar_novo_usuario(request : NovoUsuarioRequest):
    return await UsuarioBO().novo_usuario(request)

# Principal

    # Criar método que vai acessar Postgres e realizar CRUD simples.
    # > Apply a BaseDAO
    # > Seguir o padrão da Modelagem (DAO > Model) 