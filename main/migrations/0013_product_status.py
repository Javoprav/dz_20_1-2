# Generated by Django 4.2.2 on 2023-06-16 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('Активна', 'Активна'), ('Не активна', 'Не активна')], default='Не активна', max_length=50, verbose_name='Статус'),
        ),
    ]
