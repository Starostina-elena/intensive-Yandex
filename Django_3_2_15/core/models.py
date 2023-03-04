from django.db import models

from sorl.thumbnail import ImageField


class ModelForCatalog(models.Model):
    name = models.CharField('Название', max_length=150)
    is_published = models.BooleanField('Опубликовано?', default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class ModelForImage(models.Model):
    image = ImageField('изображение',
                       upload_to='')
    
    class Meta:
        abstract = True

    def __str__(self):
        return self.image.name
