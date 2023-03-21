from django.db import models


class Feedback(models.Model):
    text = models.TextField(verbose_name='текст обращения')
    created_on = models.DateTimeField(auto_now_add=True,
                                      verbose_name='дата создания')
    email = models.EmailField(verbose_name='электронная почта')
