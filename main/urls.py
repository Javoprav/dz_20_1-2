from django.urls import path
from main.apps import MainConfig
from main.views import IndexView, ProductListView, ContactView, ProductDetailView, RecordListView, RecordDetailView, \
    RecordCreateView, RecordUpdateView, RecordDeleteView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    VersionListView

app_name = MainConfig.name


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('', post_route)  # получение запроса из постмана
    path('contacts/', ContactView.as_view(), name='contacts'),  # Вывод url контакты  из views.py contacts
    path('products/', ProductListView.as_view(), name='products_list'),
    path('version/', VersionListView.as_view(), name='version_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_item'),  # url студента с переменной, в контроллере(views) так же указывается
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('records/', RecordListView.as_view(), name='records_list'),
    path('records/<slug:slug>/', RecordDetailView.as_view(), name='record_detail'),
    path('record/create/', RecordCreateView.as_view(), name='record_create'),
    path('record/update/<int:pk>/', RecordUpdateView.as_view(), name='record_update'),
    path('record/delete/<int:pk>/', RecordDeleteView.as_view(), name='record_delete'),
]