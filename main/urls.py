from django.urls import path
from main.apps import MainConfig
from main.views import IndexView, ProductListView, ContactView, ProductDetailView

app_name = MainConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('', post_route)  # получение запроса из постмана
    path('contacts/', ContactView.as_view(), name='contacts'),  # Вывод url контакты  из views.py contacts
    path('products/', ProductListView.as_view(), name='products_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_item'),  # url студента с переменной, в контроллере(views) так же указывается
]