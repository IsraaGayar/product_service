import uuid
import random
from datetime import datetime, timedelta
from decimal import Decimal
from products.models import Category, Product
from django.contrib.auth.models import User


def generate_random_data():
    """Generates random data for Category and Product models."""

    categories = []
    products = []

    category_names = ["Electronics", "Clothing", "Books", "Home & Kitchen", "Sports", "Toys", "Groceries"]
    for name in category_names:
        categories.append({
            "id": uuid.uuid4(),
            "name": name,
            "description": f"Description for {name}",
            "created_at": datetime.now() - timedelta(days=random.randint(1, 30)),
            "modified_at": datetime.now(),
        })

    product_names = [
        "Laptop", "Smartphone", "T-Shirt", "Jeans", "Novel", "Cookbook",
        "Blender", "Sofa", "Basketball", "Football", "Action Figure", "Board Game",
        "Apples", "Milk", "Bread",
    ]

    for name in product_names:
        category = random.choice(categories)
        products.append({
            "id": uuid.uuid4(),
            "name": name,
            "category_id": category["id"],
            "price": Decimal(random.uniform(10, 500)).quantize(Decimal("0.01")),
            "description": f"Description for {name}",
            "created_at": datetime.now() - timedelta(days=random.randint(1, 30)),
            "modified_at": datetime.now(),
        })

    return categories, products

def insert_data(categories, products):
    """Inserts generated data into the database."""
    for category_data in categories:
        Category.objects.create(
            id=category_data["id"],
            name=category_data["name"],
            description=category_data["description"],
            created_at=category_data["created_at"],
            modified_at=category_data["modified_at"],
        )

    for product_data in products:
        Product.objects.create(
            id=product_data["id"],
            name=product_data["name"],
            category_id=product_data["category_id"],
            price=product_data["price"],
            description=product_data["description"],
            created_at=product_data["created_at"],
            modified_at=product_data["modified_at"],
        )

def create_main_users():
    create_superuser()
    create_staffuser()
    create_user()

def create_superuser():
    user = User.objects.create(
        username='superuser', is_superuser=True
    )
    user.set_password('password')

def create_staffuser():
    user = User.objects.create(
        username='staffuser', is_staff=True
    )
    user.set_password('password')

def create_user():
    user = User.objects.create(
        username='testuser', is_superuser=True
    )
    user.set_password('password')