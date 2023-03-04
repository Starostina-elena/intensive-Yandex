# Generated by Django 3.2.15 on 2023-03-02 18:46

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20230302_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='main_image',
            field=sorl.thumbnail.fields.ImageField(height_field='300', null=True, upload_to='', verbose_name='Главное изображение', width_field='300'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=sorl.thumbnail.fields.ImageField(height_field=300, upload_to='media', width_field=300),
        ),
    ]