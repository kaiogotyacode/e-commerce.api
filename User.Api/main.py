from fastapi import FastAPI

teste = FastAPI()

@teste.get("/")
def home():
    return "API ON"