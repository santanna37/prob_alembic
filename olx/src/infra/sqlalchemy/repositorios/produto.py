#IMPORTANDO BIBLIOTECAS 

from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from sqlalchemy import *


#REPOSITORIO DE PRODUTOS 

class RepositorioProduto():

    def __init__(self, session:Session):
        self.session = session

# criar a tabela no banco de dadso 
    def criar(self, produto: schemas.Produto):
        db_produto = models.Produto(nome = produto.nome,
                                    detalhe = produto.detalhe,
                                    preco = produto.preco,
                                    disponivel = produto.disponivel,
                                    id_usuario = produto.id_usuario
                                    )

        self.session.add(db_produto)
        self.session.commit()
        self.session.refresh(db_produto)
        return db_produto


#listar a tabela no bando de dados 
    def listar(self):
        produtos = self.session.query(models.Produto).all()
        return produtos


#deletar produto 
    def deletar(self, id: int):
        st = delete(models.Produto).where(
                    models.Produto.id == id)
        
        self.session.execute(st)
        self.session.commit()
       # self.session.refresh(models.Produto)
        
       # return {f'msg': 'ID {id} foi deletado'}
    

#editar produto
    def editar(self, produto: schemas.Produto):
        st = update(models.Produto).where(
            models.Produto.id == produto.id).values(
                                        nome = produto.nome,
                                        detalhe = produto.detalhe,
                                        preco = produto.preco, 
                                        disponivel = produto.disponivel,
                                        id = produto.id
                                        )
        self.session.execute(st)
        self.session.commit()
        return produto 

