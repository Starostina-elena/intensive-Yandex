from catalog import models

from django.core import exceptions
from django.test import Client, TestCase

from parameterized import parameterized


class TestDataBaseAddItem(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.category = models.Category.objects.create(
            is_published=True,
            name='Тестовая категория',
            slug='test-category-slug',
            weight=100
        )
        cls.tag = models.Tag.objects.create(
            is_published=True,
            name='Тестовый тэг',
            slug='test-tag-slug'
        )

    def test_unable_create_one_letter(self):
        item_count = models.Item.objects.count()
        with self.assertRaises(exceptions.ValidationError):
            self.item = models.Item(
                id=1,
                name='Тестовый товар',
                category=self.category,
                text='1'
            )
            self.item.full_clean()
            self.item.save()

        self.assertEqual(models.Item.objects.count(), item_count)

    def test_unable_create_without_good_text(self):
        item_count = models.Item.objects.count()
        with self.assertRaises(exceptions.ValidationError):
            self.item = models.Item(
                id=1,
                name='Тестовый товар',
                category=self.category,
                text='11111111111'
            )
            self.item.full_clean()
            self.item.save()

        self.assertEqual(models.Item.objects.count(), item_count)

    def test_unable_create_item_with_too_long_title(self):
        item_count = models.Item.objects.count()
        with self.assertRaises(exceptions.ValidationError):
            self.item = models.Item(
                id=1,
                name='I' * 151,
                category=self.category,
                text='1'
            )
            self.item.full_clean()
            self.item.save()

        self.assertEqual(models.Item.objects.count(), item_count)

    def test_unable_create_item_without_category(self):
        item_count = models.Item.objects.count()
        with self.assertRaises(exceptions.ValidationError):
            self.item = models.Item(
                id=1,
                name='TestItem',
                text='1234'
            )
            self.item.full_clean()
            self.item.save()

        self.assertEqual(models.Item.objects.count(), item_count)

    def test_able_create_item(self):
        item_count = models.Item.objects.count()

        self.item = models.Item(
            id=1,
            name='TestItem',
            text='превосходно',
            category=self.category
        )

        self.item.full_clean()
        self.item.tags.add(TestDataBaseAddItem.tag)
        self.item.save()

        self.assertEqual(models.Item.objects.count(), item_count + 1)


class TestDataBaseAddTag(TestCase):
    def test_able_create_tag(self):
        tag_count = models.Tag.objects.count()

        self.tag = models.Tag(
            id=1,
            name='TestTag',
            slug='test_slug',
            is_published=True,
        )

        self.tag.full_clean()
        self.tag.save()

        self.assertEqual(models.Tag.objects.count(), tag_count + 1)

    def test_unable_create_long_tag(self):
        tag_count = models.Tag.objects.count()

        with self.assertRaises(exceptions.ValidationError):
            self.tag = models.Tag(
                id=1,
                name='I' * 201,
                slug='test_slug',
                is_published=True,
            )

            self.tag.full_clean()
            self.tag.save()

        self.assertEqual(models.Item.objects.count(), tag_count)

    def test_unable_create_tag_with_long_slug(self):
        tag_count = models.Tag.objects.count()

        with self.assertRaises(exceptions.ValidationError):
            self.tag = models.Tag(
                id=1,
                name='TestTag',
                slug='t' * 201,
                is_published=True,
            )

            self.tag.full_clean()
            self.tag.save()

        self.assertEqual(models.Item.objects.count(), tag_count)


class TestDataBaseAddCategory(TestCase):
    def test_able_create_category(self):
        category_count = models.Category.objects.count()

        self.category = models.Category(
            id=1,
            name='TestCategory',
            slug='test_slug',
            is_published=True,
        )

        self.category.full_clean()
        self.category.save()

        self.assertEqual(models.Category.objects.count(), category_count + 1)

    def test_unable_create_long_category(self):
        category_count = models.Category.objects.count()

        with self.assertRaises(exceptions.ValidationError):
            self.category = models.Category(
                id=1,
                name='I' * 201,
                slug='test_slug',
                is_published=True,
            )

            self.category.full_clean()
            self.category.save()

        self.assertEqual(models.Category.objects.count(), category_count)

    def test_unable_create_tag_with_long_slug(self):
        category_count = models.Category.objects.count()

        with self.assertRaises(exceptions.ValidationError):
            self.category = models.Category(
                id=1,
                name='TestCategory',
                slug='t' * 201,
                is_published=True,
            )

            self.category.full_clean()
            self.category.save()

        self.assertEqual(models.Category.objects.count(), category_count)


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
            ('convertor/0001', 200),
            ('convertor/-001', 404),
        ]
    )
    def test_catalog_item_id_re_convertor_endpoint(self, url, code):
        response = Client().get(f'/catalog/{url}')
        self.assertEqual(response.status_code, code)
