# Generated by Django 3.2.15 on 2023-03-03 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_rename_main_image2_item_main_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Photo',
            new_name='PhotoForGallery',
        ),
        migrations.AlterModelOptions(
            name='imagemodel',
            options={'verbose_name': 'главное изображение', 'verbose_name_plural': 'главные изображения'},
        ),
        migrations.RemoveField(
            model_name='item',
            name='main_image',
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='item_connected',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='catalog.item', verbose_name='Главное изображение'),
            preserve_default=False,
        ),
    ]