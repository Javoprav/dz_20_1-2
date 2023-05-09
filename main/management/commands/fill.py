import json, os
from pprint import pprint

from django.core.management import BaseCommand
from main.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Моя команда')

        Category_list_all = Category.objects.all()
        Category_list_all.delete()

        product_list_all = Product.objects.all()
        product_list_all.delete()

        os.system("python manage.py loaddata category.json")

        with open('db.json', 'r', encoding='Windows-1251') as f:
            data = json.load(f)
            f.close()

        for prod in data:
            name = Category.objects.get(pk=prod["fields"]["category"])
            prod["fields"]["category"] = name

        product_list = []
        for product in data:
            product_list.append(Product(**product["fields"]))

        Product.objects.bulk_create(product_list)