import json, os
from pprint import pprint

import psycopg2
from django.core.management import BaseCommand

from config import config
from main.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        params = config()
        conn = psycopg2.connect(dbname='postgres', **params)
        conn.autocommit = True
        cur = conn.cursor()
        # try:
        #     cur.execute(f"DROP DATABASE project")
        # except psycopg2.errors.InvalidCatalogName:
        #     print(f'psycopg2.errors.InvalidCatalogName: ОШИБКА:  база данных project не существует')
        # try:
        #     cur.execute(f"CREATE DATABASE project")
        # except psycopg2.errors.DuplicateDatabase:
        #     print('ОШИБКА:  отношение "main_category" не существует')
        # conn.close()

        # if Category.objects.all():
        #     category_list_all = Category.objects.all()
        #     category_list_all.delete()

        # if Product.objects.all():
        #     product_list_all = Product.objects.all()
        #     product_list_all.delete()

        os.system("python manage.py migrate")
        # os.system("python manage.py loaddata category.json")   # Windows-1251

        with open('category.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            f.close()

        category_list = []
        for category in data:
            category_list.append(Category(**category["fields"]))
        Category.objects.bulk_create(category_list)

        with open('db.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            f.close()

        for prod in data:
            name = Category.objects.get(pk=prod["fields"]["category"])
            prod["fields"]["category"] = name

        product_list = []
        for product in data:
            product_list.append(Product(**product["fields"]))
        Product.objects.bulk_create(product_list)