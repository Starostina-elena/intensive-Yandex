from django.contrib.auth.models import User
from django.db import models

from sorl import thumbnail


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='пользователь'
    )
    birthday = models.DateField(
        'дата рождения',
        blank=True,
        null=True,
    )
    image = thumbnail.ImageField(
        'аватарка',
        blank=True,
        null=True,
        upload_to='user_pics/'
    )
    coffee_count = models.IntegerField(
        'количество попыток сварить кофе',
        default=0,
    )

    @property
    def get_user_pic_50_50(self):
        return thumbnail.get_thumbnail(self.image,
                                       '50x50',
                                       crop='center',
                                       quality=51)

    def get_absolute_url(self):
        return f'/users/user_detail/{self.user.id}'

    class Meta:
        verbose_name = 'дополнительное поле'
        verbose_name_plural = 'дополнительные поля'
