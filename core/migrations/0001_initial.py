# Generated by Django 4.0.3 on 2022-03-04 19:54

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(
                    auto_now_add=True, verbose_name='Data de criação')),
                ('updatedAt', models.DateField(default=True, verbose_name='Ativo')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('price', models.DecimalField(
                    decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('stock', models.IntegerField(verbose_name='Estoque')),
                ('image', stdimage.models.StdImageField(
                    upload_to='products_images', verbose_name='Imagem')),
                ('slug', models.SlugField(blank=True, editable=False,
                 max_length=100, verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
