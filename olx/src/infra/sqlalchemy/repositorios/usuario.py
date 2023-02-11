#IMPORTANDO BIBLIOTECAS 

from sqlalchemy.orm import Session 
from src.schemas import schemas 
from src.infra.sqlalchemy.models import models 
from sqlalchemy import select


#REPOSITORIO DE USUARIOS 

class RepositorioUsuario():

    def __init__(self, session: Session):
       self.session = session


# criar tabela no banco de dados 
    def criar(self, usuario: schemas.Usuario):
        db_usuario = models.Usuario(nome = usuario.nome,
                                    telefone = usuario.telefone,
                                    senha = usuario.senha)
        
        self.session.add(db_usuario)
        self.session.commit()
        self.session.refresh(db_usuario)
        return db_usuario


# listar usuarios 
    def listar(self):
        selecao = select(models.Usuario)
       
        usuarios = self.session.execute(selecao).scalars().all()
        return usuarios

    #listar a tabela no bando de dados 
    # def listar(self):
    #     usuarios = self.session.query(models.Usuario).all()
    #     return usuarios