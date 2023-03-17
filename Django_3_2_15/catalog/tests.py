from catalog import models

from django.core import exceptions
from django.test import Client, TestCase
from django.urls import reverse

from parameterized import parameterized


class TestContext(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.published_category = models.Category.objects.create(
            is_published=True,
            name='Тестовая категория',
            slug='test-category-slug',
            weight=100
        )
        cls.unpublished_category = models.Category.objects.create(
            is_published=False,
            name='Тестовая категория2',
            slug='test-category-slug2',
            weight=100
        )
        cls.published_tag = models.Tag.objects.create(
            is_published=True,
            name='Тестовый тэг',
            slug='test-tag-slug'
        )
        cls.unpublished_tag = models.Tag.objects.create(
            is_published=False,
            name='Тестовый тэг2',
            slug='test-tag-slug2'
        )
        cls.published_item = models.Item(
            name='Тестовый товар',
            category=cls.published_category,
            text='превосходно',
            is_published=True,
        )
        cls.published_item_on_main = models.Item(
            name='Тестовый товар2',
            category=cls.published_category,
            text='превосходно',
            is_published=True,
            is_on_main=True,
        )
        cls.unpublished_item = models.Item(
            name='Тестовый товар3',
            category=cls.published_category,
            text='превосходно',
            is_published=False,
        )

        cls.published_category.save()
        cls.unpublished_category.save()
        cls.published_tag.save()
        cls.unpublished_tag.save()

        cls.published_item.clean()
        cls.published_item.save()
        cls.published_item_on_main.clean()
        cls.published_item_on_main.save()
        cls.unpublished_item.clean()
        cls.unpublished_item.save()

        cls.published_item.tags.add(cls.published_tag.pk)
        cls.published_item.tags.add(cls.unpublished_tag.pk)

    def test_home_page_show_context(self):
        response = Client().get(reverse('homepage:home'))
        self.assertIn('items_list', response.context)

    def test_home_page_count_item(self):
        response = Client().get(reverse('homepage:home'))
        self.assertEqual(response.context['items_list'].count(), 1)

    def test_catalog_show_context(self):
        response = Client().get(reverse('catalog:item_list'))
        self.assertIn('items_list', response.context)

    def test_catalog_count_item(self):
        response = Client().get(reverse('catalog:item_list'))
        self.assertEqual(response.context['items_list'].count(), 2)

    def test_item_detail_show_context(self):
        response = Client().get(reverse('catalog:item_detail', args=[1]))
        self.assertIn('item', response.context)
        self.assertIn('album', response.context)

    def tearDown(self):
        models.Category.objects.all().delete()
        models.Tag.objects.all().delete()
        models.Item.objects.all().delete()


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

    def tearDown(self):
        models.Category.objects.all().delete()
        models.Tag.objects.all().delete()
        models.Item.objects.all().delete()

    @parameterized.expand(
        [
            ('1',),
            ('111111',),
            ('превосходнооо',),
            ('роскошноb',),
        ]
    )
    def test_unable_create_with_bad_description(self, text):
        item_count = models.Item.objects.count()
        with self.assertRaises(exceptions.ValidationError):
            self.item = models.Item(
                id=1,
                name='Тестовый товар',
                category=self.category,
                text=text
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

    def tearDown(self):
        models.Category.objects.all().delete()
        models.Tag.objects.all().delete()
        models.Item.objects.all().delete()

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

        self.assertEqual(models.Tag.objects.count(), tag_count)

    def test_unable_create_tag_with_not_unique_slug(self):
        tag_count = models.Tag.objects.count()

        self.tag = models.Tag(
                id=1,
                name='TestTag',
                slug='test',
                is_published=True,
            )

        self.tag.full_clean()
        self.tag.save()

        with self.assertRaises(exceptions.ValidationError):
            self.tag = models.Tag(
                id=2,
                name='TestTag2',
                slug='test',
                is_published=True,
            )

            self.tag.full_clean()
            self.tag.save()

        self.assertEqual(models.Tag.objects.count(), tag_count + 1)


class TestDataBaseAddCategory(TestCase):

    def tearDown(self):
        models.Category.objects.all().delete()
        models.Tag.objects.all().delete()
        models.Item.objects.all().delete()

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

    def test_unable_create_category_with_long_slug(self):
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

    def test_unable_create_category_with_not_unique_slug(self):
        category_count = models.Category.objects.count()

        self.category = models.Category(
                id=1,
                name='TestCategory',
                slug='test',
                is_published=True,
            )

        self.category.full_clean()
        self.category.save()

        with self.assertRaises(exceptions.ValidationError):
            self.category = models.Category(
                id=2,
                name='TestCategory2',
                slug='test',
                is_published=True,
            )

            self.category.full_clean()
            self.category.save()

        self.assertEqual(models.Category.objects.count(), category_count + 1)

    @parameterized.expand(
        [
            (-1,),
            (100000000000,),
        ]
    )
    def test_unable_create_category_with_wrong_weight(self, weight):
        category_count = models.Category.objects.count()

        with self.assertRaises(exceptions.ValidationError):
            self.category = models.Category(
                id=1,
                name='TestCategory',
                slug='test',
                is_published=True,
                weight=weight,
            )

            self.category.full_clean()
            self.category.save()

        self.assertEqual(models.Category.objects.count(), category_count)
