#ROTAS DOS PEDIDOS 

#importando bibliotecas 
from fastapi import APIRouter, Depends, status
from src.schemas import schemas
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositorios.pedido import RepositorioPedidos 
from src.infra.sqlalchemy.config.database import get_db


router = APIRouter()


#criando rotas 

#rota criar pedido 
@router.post('/pedidos')
def criar(pedido: schemas.Pedido, session: Session = Depends(get_db)):
    pedido_criado = RepositorioPedidos(session).criar(pedido)
    return pedido_criado

@router.get('/pedidos')
def listar(session: Session = Depends(get_db)):
    produtos = RepositorioPedidos(session).listar()