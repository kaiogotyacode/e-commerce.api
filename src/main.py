# import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from presentation.routers.usuario_routes import router as usuario_router
from presentation.routers.token_routes import router as token_router
from presentation.routers.produto_routes import router as produto_router
from presentation.routers.exibicao_produto_routes import router as exibicao_produto_router
from presentation.routers.banner_produto_routes import router as banner_produto_router

# TODO: Aprender a como separar as "Tags" (Default) por Controllers, de forma individual/segregada.

app = FastAPI(
    title="E-commerce API",
    description="API para gerenciamento de e-commerce",
    version="1.0.0"
)


@app.get("/", include_in_schema=False)
def home():
    return RedirectResponse(url="/docs")

app.include_router(usuario_router)
app.include_router(produto_router)
app.include_router(exibicao_produto_router)
app.include_router(banner_produto_router)
app.include_router(token_router)