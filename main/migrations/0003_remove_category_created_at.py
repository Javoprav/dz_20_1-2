# Generated by Django 4.2.1 on 2023-05-06 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created_at',
        ),
    ]
