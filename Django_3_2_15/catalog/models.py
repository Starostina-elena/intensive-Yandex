from core.models import ModelForCatalog
from core.validators import validator_word_good

from django.core import validators
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from django_cleanup import cleanup

from sorl.thumbnail import ImageField, get_thumbnail


class Tag(ModelForCatalog):
    slug = models.SlugField('Slug',
                            max_length=200,
                            unique=True,
                            help_text='Укажите slug')

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


@cleanup.select
class PhotoForGallery(models.Model):
    image = ImageField('изображение',
                       upload_to='')
    item = models.ForeignKey('Item',
                             verbose_name='изображение',
                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'

    def __str__(self):
        return self.image.name


class Item(ModelForCatalog):
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

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def get_absolute_url(self):
        return reverse('catalog:item_detail', args=[self.id])


@cleanup.select
class ImageModel(models.Model):

    image = ImageField('главное изображение',
                       upload_to='',
                       null=True,)
    item_connected = models.ForeignKey('Item',
                                       on_delete=models.CASCADE,
                                       verbose_name='главное изображение',
                                       )

    def get_main_image_300_300(self):
        return get_thumbnail(self.image,
                             '300x300',
                             crop='center',
                             quality=51)

    def image_tmb(self):
        img = ImageModel.objects.get(item_connected=self.id)
        if img:
            return mark_safe(
                f'<img src="{img.image.url}" width="50">'
            )
        return 'Изображения нет'
    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True

    class Meta:
        verbose_name = 'главное изображение'
        verbose_name_plural = 'главные изображения'
