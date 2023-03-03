# Generated by Django 3.2.15 on 2023-03-02 18:50

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20230302_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='main_image',
            field=sorl.thumbnail.fields.ImageField(height_field='300px', null=True, upload_to='', verbose_name='Главное изображение', width_field='300px'),
        ),
    ]
