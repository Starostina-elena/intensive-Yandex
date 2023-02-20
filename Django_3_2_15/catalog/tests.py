from django.test import Client, TestCase

from parameterized import parameterized


class StaticUrlTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    @parameterized.expand(
        [
            ('5', 200),
            ('zfsd', 404),
            ('-5', 404),
            ('-0', 404),
        ]
    )
    def test_catalog_item_id_classic_endpoint(self, url, code):
        response = Client().get(f'/catalog/{url}')
        self.assertEqual(response.status_code, code)

    @parameterized.expand(
        [
            ('convertor/5', 200),
            ('re/5', 200),
            ('convertor/-5', 404),
            ('re/-5', 404),
            ('convertor/afaf', 404),
            ('re/zkjcbds', 404),
            ('convertor/0', 404),
            ('re/0', 404),
            ('convertor/-0', 404),
            ('re/-0', 404),
            ('convertor/0001', 404),
            ('convertor/-001', 404),
        ]
    )
    def test_catalog_item_id_re_convertor_endpoint(self, url, code):
        response = Client().get(f'/catalog/{url}')
        self.assertEqual(response.status_code, code)
