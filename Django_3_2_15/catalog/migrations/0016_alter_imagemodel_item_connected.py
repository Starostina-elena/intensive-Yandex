# Generated by Django 3.2.15 on 2023-03-04 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_auto_20230304_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='item_connected',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalog.item', verbose_name='главное изображение'),
        ),
    ]
