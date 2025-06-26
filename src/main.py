from fastapi import FastAPI

# TODO: Aprender a como separar as "Tags" (Default) por Controllers, de forma individual/segregada.

app = FastAPI()

@app.get("/")
def home():
    return "API ON"

@app.get("/teste")
def teste():
    return "API ON - TESTE"

# Principal

    # Criar método que vai acessar Postgres e realizar CRUD simples.
    # > Apply a BaseDAO
    # > Seguir o padrão da Modelagem (DAO > Model) 