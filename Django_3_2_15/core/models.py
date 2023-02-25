from django.db import models


class ModelForCatalog(models.Model):
    name = models.CharField('Название', max_length=150)
    is_published = models.BooleanField('Опубликовано?', default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
