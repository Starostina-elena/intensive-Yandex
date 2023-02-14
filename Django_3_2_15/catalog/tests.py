from django.test import Client, TestCase


class StaticUrlTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)
        response = Client().get('/catalog/5')
        self.assertEqual(response.status_code, 200)
