from core.models import ModelForCatalog
from core.validators import validator_word_good

from django.core import validators
from django.db import models


class Tag(ModelForCatalog):
    slug = models.SlugField('Slug',
                            max_length=200,
                            unique=True,
                            help_text='Укажите slug')

    class Meta:
        verbose_name = 'тэг'
        verbose_name_plural = 'тэги'


class Category(ModelForCatalog):
    slug = models.SlugField('Slug',
                            max_length=200,
                            unique=True,
                            help_text='Укажите slug')
    weight = models.PositiveSmallIntegerField('Вес',
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


class Item(ModelForCatalog):
    text = models.TextField('Описание',
                            help_text='Укажите описание товара',
                            validators=[
                                validator_word_good
                            ])

    category = models.ForeignKey('Category',
                                 on_delete=models.CASCADE,
                                 related_name='items',
                                 verbose_name='Категория',
                                 help_text='Укажите категорию')
    tags = models.ManyToManyField(Tag, verbose_name='Тэги',
                                  help_text='Выберите тэги.')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
