#IMPORTAÇÃO DE BASE

from pydantic import BaseModel
from typing import Optional, List




#  SCHEMAS DAS TABELAS


#tabela de produtos
class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhe: str
    preco: float
    disponivel: bool = False
    #colunas de relacionamento
    id_usuario: Optional[int] 
    

    #classe obrigatoria em todas os schemas
    class Config:
        orm_mode = True



#tabela de usuario 
class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    senha: str 

    #classe obrigatória em todos os schemas
    class Config:
        orm_mode = True



class Pedido(BaseModel):
    id: Optional[int] = None
    nome: str
    cliente: Optional[str]
    quantidade: int
    local_entrega: Optional[str]
    tipo_entrega: bool = False
    #colunas de relacionamento
    id_produto: Optional[int]
    id_usuario: Optional[int]

    #classe obrigatoria
    class Config:
        orm_mode = True 
