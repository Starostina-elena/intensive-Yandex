from django.test import Client, TestCase


class StaticUrlTests(TestCase):
    def test_coffee_endpoint(self):
        response = Client().get('/coffee/')
        self.assertContains(response, 'Я чайник', status_code=418)
