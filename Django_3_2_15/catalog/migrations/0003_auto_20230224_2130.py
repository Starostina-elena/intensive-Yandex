# Generated by Django 3.2.15 on 2023-02-24 17:30

import catalog.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20230224_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True, unique=True, validators=[django.core.validators.MaxLengthValidator(200)]),
        ),
        migrations.AddField(
            model_name='category',
            name='weight',
            field=models.PositiveSmallIntegerField(default=100),
        ),
        migrations.AddField(
            model_name='item',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='item',
            name='text',
            field=models.TextField(help_text='Укажите описание товара', null=True, validators=[catalog.models.validator_word_good], verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='tag',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(null=True, unique=True, validators=[django.core.validators.MaxLengthValidator(200)]),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
