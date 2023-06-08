import json, os
from pprint import pprint

import psycopg2
from django.core.management import BaseCommand

from config import config
from main.models import Product, Category, Record


class Command(BaseCommand):

    def handle(self, *args, **options):
        # params = config()
        # conn = psycopg2.connect(dbname='postgres', **params)
        # conn.autocommit = True
        # cur = conn.cursor()
        #
        # try:
        #     cur.execute(f"CREATE DATABASE project")
        # except psycopg2.errors.DuplicateDatabase:
        #     print('ОШИБКА:  отношение "main_category" не существует')
        # conn.close()

        try:
            os.system("python manage.py migrate")
        except Exception:
            print('ОШИБКА:  Не правильная команда')
        try:
            os.system("python3 manage.py migrate")
        except Exception:
            print('ОШИБКА:  Не правильная команда')

        with open('data_record_1.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            f.close()

        record_list = []
        for record in data:
            record_list.append(Record(**record["fields"]))
        Record.objects.bulk_create(record_list)