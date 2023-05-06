# Generated by Django 4.2.1 on 2023-05-06 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, max_length=15000, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, max_length=15000, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='Изображение')),
                ('category', models.CharField(max_length=150, verbose_name='Категория')),
                ('price_for_pickup', models.IntegerField(verbose_name='Цена за покупку')),
                ('date_of_creation', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('last_modified_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего изменения')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
                'ordering': ('name', 'category', 'price_for_pickup', 'date_of_creation'),
            },
        ),
    ]
