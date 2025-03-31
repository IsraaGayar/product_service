from django.core.management.base import BaseCommand
from product_service.data_generator import create_main_users, generate_random_data, insert_data

class Command(BaseCommand):
    help = 'Populates the database with sample data.'

    def handle(self, *args, **options):
        categories, products = generate_random_data()
        insert_data(categories, products)
        create_main_users()
        self.stdout.write(self.style.SUCCESS('Successfully populated database.'))