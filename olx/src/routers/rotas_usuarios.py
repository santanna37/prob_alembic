#  ROTAS DE PRODUTOS 

#importando bibliotecas 
from fastapi import APIRouter, Depends, status
from src.schemas import schemas
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
from src.infra.sqlalchemy.config.database import get_db


#CRIANDO ROTAS 

router = APIRouter()


#rotas de usuarios
@router.post('/usuarios', status_code = status.HTTP_201_CREATED, response_model = schemas.Usuario )
def criar_usuario(usuario: schemas.Usuario, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado



@router.get('/usuarios', status_code = status.HTTP_202_ACCEPTED)
def listar_usuarios(session: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios

