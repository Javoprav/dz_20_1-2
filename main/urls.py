from django.urls import path

from main.apps import MainConfig
from main.views import index, contacts, products, product

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    # path('', post_route)  # получение запроса из постмана
    path('contacts/', contacts, name='contacts'),  # Вывод url контакты  из views.py contacts
    path('products/', products, name='products_list'),
    path('product/<int:pk>/', product, name='product_item'),  # url студента с переменной, в контроллере(views) так же указывается
]