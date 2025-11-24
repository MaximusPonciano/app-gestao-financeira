from fastapi import FastAPI

from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Transacoes(BaseModel):
    descricao: str
    valor: float
    tipo: str
    categoria: str
    data: Optional[str] = None

banco_dados = []

@app.post('/transacoes')
def criar_transacoes(transacoes: Transacoes):
    banco_dados.append(transacoes)
    return {"mensagem": "Transação salva com sucesso!", "dados": transacoes}

@app.get('/transacoes')
def listar_transacoes():
    return banco_dados