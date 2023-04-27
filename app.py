from fastapi import FastAPI
from routes.user import products

app = FastAPI()

app.include_router(route_products)

