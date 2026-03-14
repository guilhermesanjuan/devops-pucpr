"""Módulo de API para a matéria de DevOps."""
import random

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """Retorna uma mensagem de boas-vindas."""
    return {"Hello": "World", "Random_Number": random.randint(1, 100)}

@app.get("/status")
def get_status():
    """Retorna o status da API."""
    return {"status": "ok"}