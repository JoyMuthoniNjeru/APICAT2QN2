import requests
import json

# Base URL of the API
BASE_URL = "http://127.0.0.1:8000/api/products/"

# Function to add a new product (POST request)
def add_product(name, description, price):
    # Data to be sent as JSON
    data = {
        "name": name,
        "description": description,
        "price": price
    }

    # Send POST request to create a new product
    response = requests.post(BASE_URL, json=data)

    # Check if the request was successful
    if response.status_code == 201:
        print(f"Product '{name}' created successfully!")
        print("Response:", response.json())
    else:
        print(f"Failed to create product '{name}'.")
        print("Error:", response.json())

# Function to retrieve and print all products (GET request)
def get_all_products():
    # Send GET request to retrieve all products
    response = requests.get(BASE_URL)

    # Check if the request was successful
    if response.status_code == 200:
        products = response.json()
        print("All Products:")
        for product in products:
            print(f"- {product['name']}: {product['description']} (Price: {product['price']})")
    else:
        print("Failed to retrieve products.")
        print("Error:", response.json())

# Example Usage:
if __name__ == "__main__":
    # Add a new product
    add_product("Smartwatch", "A high-tech smartwatch.", 199.99)

    # Retrieve and print all products
    get_all_products()
