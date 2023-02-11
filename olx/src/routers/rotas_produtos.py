#  ROTAS DE PRODUTOS 

#importando bibliotecas 
from fastapi import APIRouter, Depends 
from src.schemas import schemas
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
from src.infra.sqlalchemy.config.database import get_db


#CRIANDO ROTAS 

router = APIRouter() 

# rotas de produtos
@router.post('/produtos')
def criar_produto(produto: schemas.Produto, session: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(session).criar(produto)
    return produto_criado
    


@router.get('/produtos')
def listar_produtos(session: Session = Depends(get_db)):
    produtos = RepositorioProduto(session).listar()
    return produtos



@router.put('/produtos')
def editar_produtos(produto: schemas.Produto, session: Session = Depends(get_db)):
    RepositorioProduto(session).editar(produto)
    return produto



@router.delete('/produtos/{id}')
def apagar_produtos(id: int, session: Session = Depends(get_db)):
    a = id
    RepositorioProduto(session).deletar(id)
    return {'iten  deltado'}
