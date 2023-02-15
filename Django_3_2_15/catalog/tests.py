from django.test import Client, TestCase

from parameterized import parameterized


class StaticUrlTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    @parameterized.expand(
        [
            ('/catalog/5', 200),
            ('/catalog//5', 200),
            ('/catalog/sfhbs/5', 200),
            ('/catalog/-5', 404),
            ('/catalog//-5', 404),
            ('/catalog/sfhbs/-5', 404)
        ]
    )
    def test_catalog_item_id_endpoint(self, url, code):
        response = Client().get(url)
        self.assertEqual(response.status_code, code)
