# Product API
-This project provides a simple REST API to manage products using Django. The API includes endpoints to create and retrieve products, with fields like name, description, and price.

## Setup Instructions

Step 1: Clone the Repository
git clone https://github.com/your-username/product-api.git

Step 2: Create and Activate a Virtual Environment
It is recommended to use a virtual environment to manage project dependencies. Run the following commands:

1. Create a virtual environment:python -m venv venv
2. Activate the virtual environment:.\venv\Scripts\activate

Step 3: Install Dependencies
pip install django requests

Step 4: Set Up the Django Project
Run migrations to set up the database:python manage.py migrate

Step 5: Run the Django Development Server
python manage.py runserver

Step 6: Testing the API Manually or with Python Script

## API Endpoints

1. POST /products: Create a New Product
    Request:-URL: /api/products/
            -Method: POST

    Response:
        Status: 201 Created

2. GET /products: Retrieve All Products
   Request:-URL: /api/products/
           -Method: GET

    Response:
        Status: 200 OK