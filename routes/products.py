from fastapi import APIRouter, Response, status, HTTPException
from config.db import conn
from models.products import products
from schemas.product import Product
from tools.handlers import Handlers

flag = Handlers()

route_product = APIRouter()

# Route to create a product
@route_product.post('/products', tags=["Products"])
def create_product(product: Product):
    # Create the new product dictionary
    new_item = {'name': product.name, 'description': product.description,
                'price': product.price, 'quantity': product.quantity,
                'color': product.color, 'serial': product.serial}
    try:
        # Insert the new product into the database
        result = conn.execute(products.insert().values(new_item))
        return 'Product created successfully.', conn.execute(products.select().where(products.c.id == result.lastrowid)).first()
    except Exception as e:
        print(f'Error creating product: {e}')
        return 'Error creating product'

    # Commiting changes
    conn.commit()


# Route to search all products
@route_product.get('/products', tags=["Products"])
def get_products():
    return conn.execute(products.select()).fetchall()


# Route to search products by ID
@route_product.get('/products/{id}', tags=["Search products by ID"])
def get_product(id: int):
    # Check if product exists
    if flag.select(conn, products):
        raise HTTPException(status_code=404, detail="Item not found")

     # Getting the product by ID of the database
    result = conn.execute(products.select().where(
        products.c.id == id)).first()
    return result

# Route to update a product property by ID
@route_product.put('/products/{id}', tags=["Products"])
def update_product(id: int, product: Product):
    # Check if product already exists
    if flag.select(conn, products):
        raise HTTPException(status_code=404, detail="Item not found")

    # Updating the product of the database
    result = conn.execute(products.update().values(
        name=product.name, description=product.description,
        price=product.price, quantity=product.quantity,
        color=product.color, serial=product.serial
    ).where(products.c.id == id))
    return 'Product updated successfully! The new properties is:', conn.execute(products.select().where(products.c.id == id)).first()

    # Commiting changes
    conn.commit()


#Route to delete product by ID
@route_product.delete('/products/{id}', tags=["Products"])
def delete_product(id: int):
    # Check if item already exists
    if flag.select(conn, products):
        raise HTTPException(status_code=404, detail="Item not found")

    # Deleting the product of the database
    old_properties = conn.execute(
        products.select().where(products.c.id == id)).first()
    result = conn.execute(products.delete().where(products.c.id == id))
    return f'product {old_properties.name} deleted successfully.'
    
    # Commiting changes
    conn.commit()
