from django.core import validators
from django.db import models


class ModelForCatalog(models.Model):
    name = models.CharField(max_length=150)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(validators=[
                                validators.MaxLengthValidator(200)
                            ],
                            unique=True,
                            null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
