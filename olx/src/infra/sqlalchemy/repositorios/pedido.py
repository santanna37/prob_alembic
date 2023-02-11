#REPOSITORIO DE PEDIDOS
#bibliotecas 
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from sqlalchemy import *


#REPOSITORIOS 

class RepositorioPedidos():
    def __init__(self, session:Session):
        self.session = session

    
    #criar pedidos 
    def criar(self, pedido: schemas.Pedido):
        db_pedido = models.Pedido(
                        nome = pedido.nome,
                        cliente = pedido.cliente,
                        quantidade = pedido.quantidade,
                        local_entrega = pedido.local_entrega,
                        tipo_entrega = pedido.tipo_entrega,
                        id_produto = pedido.id_produto,
                        id_usuario = pedido.id_usuario
       )
  
        self.session.add(db_pedido)
        self.session.commit()
        self.session.refresh(db_pedido)
        return db_pedido


    #listar pedidos
    def listar(self, pedido: models.Pedido):
        st = select(pedido)
        pedidos = self.session.execute(st).scalar().all()
        return pedidos