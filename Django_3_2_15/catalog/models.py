from Core.models import ModelForCatalog

from django.core import exceptions
from django.db import models


def validator_word_good(value):
    if 'превосходно' not in value.lower() and 'роскошно' not in value.lower():
        raise exceptions.ValidationError('В тексте должно быть '
                                         'слово "превосходно" или "роскошно"')


class Tag(ModelForCatalog):
    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Category(ModelForCatalog):
    weight = models.PositiveSmallIntegerField(default=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Item(models.Model):
    name = models.CharField(max_length=150)
    text = models.TextField('Описание',
                            help_text='Укажите описание товара',
                            validators=[
                                validator_word_good
                            ],
                            null=True)

    is_published = models.BooleanField('Опубликовано?', default=True)

    category = models.ForeignKey('Category',
                                 on_delete=models.CASCADE,
                                 related_name='items',
                                 null=True,)
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name[:15]
