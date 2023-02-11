#IMPORTANDO BIBLIOTECAS

from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey
from src.infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import relationship




#MODELOS DAS TABELAS


#modelo da tabela produto 
class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key = True, index = True)
    nome = Column(String)
    detalhe = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)
    #colunas de relacionamento - usuario
    usuario = relationship('Usuario', back_populates = 'produtos')
    id_usuario = Column(Integer, ForeignKey('usuario.id', name = 'fk_usuario'))
    #colunas de relacionamento - pedidos
    pedido = relationship('Pedido', back_populates = 'produto')


#modelo da tabela usuario
class Usuario(Base):

    __tablename__ = 'usuario'

    id = Column(Integer, primary_key = True, index = True)
    nome = Column(String)
    telefone = Column(String)
    senha = Column(String)
    #colunas de ralacionamento - usuario
    produto = relationship('Produto', back_populates = 'usuario')
    #colunas de relacionamento - pedidos
    pedido = relationship('Pedido', back_populates = 'usuario')



#modelo de tabela pedidos
class Pedido(Base):

    __tablename__ = 'pedido'

    id =  Column(Integer, primary_key = True, index = True)
    nome = Column(String)
    cliente = Column(String)
    quantidade = Column(String)
    local_entrega = Column(String)
    tipo_entrega = Column(Boolean)
    #colunas de relacionamento - produto
    id_produto = Column(Integer, ForeignKey(Produto.id, 'fk_produto'))
    produto = relationship('Produto', back_populates = 'pedido')
    #colunas de relacionamento - usuario
    id_usuario = Column(Integer, ForeignKey(Usuario.id, 'fk_usuario'))
    usuario = relationship('Usuario', back_populates = 'pedido')