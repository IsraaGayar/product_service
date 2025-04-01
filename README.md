# product_service
product_service is a Django REST Framework app managing products and users, demonstrating optimized database queries and data serialization
# Product and User Service API

This Django REST Framework application provides APIs for managing products, categories, and users. It also includes token-based authentication using JWT.

## Features

-   **Product Management:**
    -   CRUD operations for products.
    -   Filtering, searching, and ordering of products.
    -   API endpoint to retrieve the top 2 most expensive products per category.
-   **Category Management:**
    -   CRUD operations for categories.
    -   Searching and ordering of categories.
-   **User Management:**
    -   CRUD operations for users.
    -   JWT token-based authentication for user login.
-   **Optimized Database Queries:**
    -   Efficient database queries to minimize load and improve performance.
-   **Data Serialization:**
    -   Clean and efficient data serialization using Django REST Framework serializers.


## Requirements

-   Python 3.x
-   Django==5.1.7
-   Django REST Framework==3.15.2
-   Django Filter==25.1
-   djangorestframework-simplejwt==5.5.0
-   PyJWT==2.9.0
-   asgiref==3.8.1
-   sqlparse==0.5.3

## Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/IsraaGayar/product_service.git](https://github.com/IsraaGayar/product_service.git)
    cd product_service
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Populate the database with test data:**

    ```bash
    python manage.py populate_data
    ```

6.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## Usage

### API Endpoints

-   **Products:**
    -   `GET /products/products/`: List all products.
    -   `POST /products/products/`: Create a new product.
    -   `GET /products/products/{id}/`: Retrieve a specific product.
    -   `PUT /products/products/{id}/`: Update a product.
    -   `DELETE /products/products/{id}/`: Delete a product.
-   **Categories:**
    -   `GET /products/categories/`: List all categories.
    -   `POST /products/categories/`: Create a new category.
    -   `GET /products/categories/{id}/`: Retrieve a specific category.
    -   `PUT /products/categories/{id}/`: Update a category.
    -   `DELETE /products/categories/{id}/`: Delete a category.
-   **Top Expensive Products:**
    -   `GET /products/top-expensive/`: List the top 2 most expensive products per category.
-   **Users:**
    -   `GET /users/`: List all users.
    -   `POST /users/`: Create a new user.
    -   `GET /users/{id}/`: Retrieve a specific user.
    -   `PUT /users/{id}/`: Update a user.
    -   `DELETE /users/{id}/`: Delete a user.
-   **Token Authentication:**
    -   `POST users/token/`: Obtain JWT access and refresh tokens.

### Testing

To run the api tests, use the following command:

```bash
python manage.py test