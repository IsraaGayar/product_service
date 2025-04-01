from django.contrib.auth.models import Permission
from rest_framework.test import APIClient
from product_service.base_tests import BaseTestCase
from products.models import Category


class TestUserAPI(BaseTestCase):
    staff_auth_data = {'username': 'staffuser', 'password': 'password'}
    superuser_auth_data = {'username': 'superuser', 'password': 'password'}
    user_auth_data = {'username': 'testuser', 'password': 'password'}

    fixtures = [
                '../fixtures/users_data.json',
                '../fixtures/products_data.json',
                ]
    rest_client = APIClient()

    def setUp(self):
        self.random_category = Category.objects.first()
        self.category_data =  {"name": "new category", "descroption": "category description"}

    def test_list_categories(self):
        self.rest_client.logout()
        response = self.rest_client.get(
            '/products/categories/', format='json')
        self.assertEqual(response.status_code, 200)
        count = response.data['count']
        data = response.data['results']
        self.assertEqual( count,7)

    def test_list_categories_with_search_name(self):
        self.rest_client.logout()
        response = self.rest_client.get(
            '/products/categories/?search=Clothing', format='json')
        self.assertEqual(response.status_code, 200)
        count = response.data['count']
        data = response.data['results']
        self.assertEqual( count,1)

    def test_create_category_main_user(self):
        "main user shouldnt create category"
        self.set_client_credentials(self.user_auth_data)
        response = self.rest_client.post(
            '/products/categories/', self.category_data, format='json')
        self.assertEqual(response.status_code, 403)

    def test_delete_category_main_user(self):
        "main user should be able to delete category"
        self.set_client_credentials(self.user_auth_data)
        id = self.random_category.id.__str__()
        response = self.rest_client.delete(
            f'/products/categories/{id}/',
            format='json')
        self.assertEqual(response.status_code, 403)
        self.assertTrue(Category.objects.filter(pk=id).exists())


    def test_create_category_staff_user(self):
        "staff user should be able to create category"
        self.set_client_credentials(self.staff_auth_data)
        response = self.rest_client.post(
            '/products/categories/', self.category_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], self.category_data['name'])

    def test_delete_category_staff_user(self):
        "staff user should be able to delete category"
        self.set_client_credentials(self.staff_auth_data)
        id = self.random_category.id.__str__()
        response = self.rest_client.delete(
            f'/products/categories/{id}/',
            format='json')
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Category.objects.filter(pk=id).exists())


    def test_create_category_superuser(self):
        "super user should be able to create category"
        self.set_client_credentials(self.superuser_auth_data)
        response = self.rest_client.post(
            '/products/categories/',  self.category_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], self.category_data['name'])

