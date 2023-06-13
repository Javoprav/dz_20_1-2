# Generated by Django 4.2.2 on 2023-06-12 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='токен'),
        ),
        migrations.AddField(
            model_name='user',
            name='token_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='время создания токена'),
        ),
    ]