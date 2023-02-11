#IMPORTANDO AS BLIBIOTECAS 

from fastapi import FastAPI
from src.infra.sqlalchemy.config.database import criar_db
from src.routers import rotas_produtos, rotas_usuarios, rotas_pedidos


#criando app e banco de dados 
criar_db()

app = FastAPI()

# CRIANDO ROTAS  

#rotas de produtos
app.include_router(rotas_produtos.router)

#rotas de usuarios
app.include_router(rotas_usuarios.router)

#rotas de pedidos 
app.include_router(rotas_pedidos.router)




