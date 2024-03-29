# Generated by Django 3.2.15 on 2023-03-02 19:21

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_item_main_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', sorl.thumbnail.fields.ImageField(null=True, upload_to='', verbose_name='Главное изображение')),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='main_image',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='main_image2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.imagemodel', verbose_name='Главное изображение'),
        ),
    ]
