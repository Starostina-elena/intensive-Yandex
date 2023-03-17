from core.models import ModelForCatalog, ModelForImage
from core.validators import validator_word_good

from django.core import validators
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from sorl.thumbnail import get_thumbnail


class Tag(ModelForCatalog):
    slug = models.SlugField('слаг',
                            max_length=200,
                            unique=True,
                            help_text='Укажите слаг')

    class Meta:
        verbose_name = 'тэг'
        verbose_name_plural = 'тэги'


class Category(ModelForCatalog):
    slug = models.SlugField('слаг',
                            max_length=200,
                            unique=True,
                            help_text='Укажите слаг')
    weight = models.PositiveSmallIntegerField('вес',
                                              default=100,
                                              help_text='Чем меньше вес, '
                                              'тем раньше товар в выдаче',
                                              validators=[
                                                validators.MinValueValidator(
                                                    0
                                                ),
                                                validators.MaxValueValidator(
                                                    32767
                                                )
                                              ])

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class PhotoForGallery(ModelForImage):

    item = models.ForeignKey('Item',
                             verbose_name='изображение',
                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'


class ItemManager(models.Manager):
    def published(self):
        return (
            self.get_queryset()
            .filter(is_published=True)
            .filter(category__is_published=True)
            .select_related(Item.category.field.name,
                            Item.imagemodel.related.name)
            .prefetch_related(
                models.Prefetch(
                    Item.tags.field.name,
                    queryset=Tag.objects.filter(is_published=True).only('name')
                )
            ).only(Item.name.field.name,
                   Item.text.field.name,
                   f'{Item.category.field.name}_{Category.id.field.name}',
                   f'{Item.category.field.name}__{Category.name.field.name}',
                   f'{Item.imagemodel.related.name}__'
                   f'{ImageModel.image.field.name}')
        )


class Item(ModelForCatalog):
    objects = ItemManager()

    text = models.TextField('описание',
                            help_text='Укажите описание товара',
                            validators=[
                                validator_word_good
                            ])

    category = models.ForeignKey('Category',
                                 on_delete=models.CASCADE,
                                 related_name='item',
                                 verbose_name='категория',
                                 help_text='Укажите категорию')
    tags = models.ManyToManyField(Tag, verbose_name='тэги',
                                  help_text='Выберите тэги.')

    is_on_main = models.BooleanField('отображать товар на главной?',
                                     help_text='Укажите, должен ли товар '
                                     'отображаться на главной',
                                     default=False)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def get_absolute_url(self):
        return reverse('catalog:item_detail', args=[self.id])


class ImageModel(ModelForImage):

    item_connected = models.OneToOneField('Item',
                                          on_delete=models.CASCADE,
                                          verbose_name='главное изображение',
                                          )

    @property
    def get_main_image_50_50(self):
        return get_thumbnail(self.image,
                             '50x50',
                             crop='center',
                             quality=51)

    @property
    def get_main_image_300_200(self):
        return get_thumbnail(self.image,
                             '300x200',
                             crop='center',
                             quality=51)

    def image_tmb(self):
        img = ImageModel.objects.get(item_connected=self.id)
        if img:
            return mark_safe(
                f'<img src="{img.get_main_image_50_50.url}">'
            )
        return 'Изображения нет'
    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True

    class Meta:
        verbose_name = 'главное изображение'
        verbose_name_plural = 'главные изображения'
