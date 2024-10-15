from fastapi import FastAPI
from .store.db import StoreDB
from .routes import router_cart, router_item
from .store.data import ShopAPIDataSource
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title='Shop API')
Instrumentator().instrument(app).expose(app)

app.include_router(router_cart)
app.include_router(router_item)

data = ShopAPIDataSource()
