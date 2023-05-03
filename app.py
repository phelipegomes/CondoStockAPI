from fastapi import FastAPI
from routes.products import route_product

app = FastAPI(
    title='CondoStock API',
    description='API created to control stock products',
    openapi_tags = [{
        'name': 'Products',
        'description': 'CRUD operations for products'
    }]
)

app.include_router(route_product)

