from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "API ON"

@app.get("/teste")
def teste():
    return "API ON - TESTE"