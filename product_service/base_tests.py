from django.test import TestCase


class BaseTestCase(TestCase):
    def set_client_credentials(self, auth_data):
        response = self.rest_client.post('/users/token/', auth_data)
        self.rest_client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + response.data['access']
        )
