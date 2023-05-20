from django.urls import path
from main.apps import MainConfig
from main.views import IndexView, ProductListView, ContactView, ProductDetailView, RecordListView, RecordDetailView, \
    RecordCreateView, RecordUpdateView, RecordDeleteView

app_name = MainConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('', post_route)  # получение запроса из постмана
    path('contacts/', ContactView.as_view(), name='contacts'),  # Вывод url контакты  из views.py contacts
    path('products/', ProductListView.as_view(), name='products_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_item'),  # url студента с переменной, в контроллере(views) так же указывается
    path('records/', RecordListView.as_view(), name='records_list'),
    path('records/<slug:slug>/', RecordDetailView.as_view(), name='record_detail'),
    path('record/create/', RecordCreateView.as_view(), name='record_create'),
    path('record/update/<int:pk>/', RecordUpdateView.as_view(), name='record_update'),
    path('record/delete/<int:pk>/', RecordDeleteView.as_view(), name='record_delete'),
]