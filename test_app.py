from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

# Test create_product route
def test_create_product():
    product = {"name": "Test Product", "description": "A product created for testing purposes", 
               "price": 10.99, "quantity": 50, "color": "red", "serial": "123456"}
    response = client.post("/products", json=product)
    assert response.status_code == 200
    assert response.json()[0] == "Product created successfully."

# Test get_products route
def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200

# Test get_product route
def test_get_product():
    # First, create a new product for testing purposes
    product = {"name": "Test Product", "description": "A product created for testing purposes", 
               "price": 10.99, "quantity": 50, "color": "red", "serial": "123456"}
    client.post("/products", json=product)
    # Then, get the id of the last inserted product
    last_id = client.get("/products").json()[-1]['id']
    # Test value returned
    print(last_id)
    # Finally, test the get_product routes
    response = client.get(f"/products/{last_id}")
    assert response.status_code == 200

# Test update_product route
def test_update_product():
    # First, create a new product for testing purposes
    product = {"name": "Test Product", "description": "A product created for testing purposes", 
               "price": 10.99, "quantity": 50, "color": "red", "serial": "123456"}
    client.post("/products", json=product)
    # Then, get the id of the last inserted product
    last_id = client.get("/products").json()[-1]['id']
    # Update the product
    updated_product = {"name": "Test Product Updated", "description": "A product created for testing purposes", 
                       "price": 9.99, "quantity": 40, "color": "blue", "serial": "123456"}
    response = client.put(f"/products/{last_id}", json=updated_product)
    assert response.status_code == 200

# Test delete_product route
def test_delete_product():
    # First, create a new product for testing purposes
    product = {"name": "Test Product", "description": "A product created for testing purposes", 
               "price": 10.99, "quantity": 50, "color": "red", "serial": "123456"}
    client.post("/products", json=product)
    # Then, get the id of the last inserted product
    last_id = client.get("/products").json()[-1]['id']
    # Finally, test the delete_product route
    response = client.delete(f"/products/{last_id}")
    assert response.status_code == 200
