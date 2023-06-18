from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from main.apps import MainConfig
from main.views import IndexView, ProductListView, ContactView, ProductDetailView, RecordListView, RecordDetailView, \
    RecordCreateView, RecordUpdateView, RecordDeleteView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    VersionListView, CategoriesListView

app_name = MainConfig.name


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('', post_route)  # получение запроса из постмана
    path('contacts/', ContactView.as_view(), name='contacts'),  # Вывод url контакты  из views.py contacts
    path('products/', ProductListView.as_view(), name='products_list'),
    path('categories/', CategoriesListView.as_view(), name='categories_list'),
    path('version/', VersionListView.as_view(), name='version_list'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_item'), # url студента с переменной, в контроллере(views) так же указывается
    path('product/create/', never_cache(ProductCreateView.as_view()), name='product_create'),
    path('product/update/<int:pk>/', never_cache(ProductUpdateView.as_view()), name='product_update'),
    path('product/delete/<int:pk>/', never_cache(ProductDeleteView.as_view()), name='product_delete'),
    path('records/', RecordListView.as_view(), name='records_list'),
    path('records/<slug:slug>/', RecordDetailView.as_view(), name='record_detail'),
    path('record/create/', never_cache(RecordCreateView.as_view()), name='record_create'),
    path('record/update/<int:pk>/', never_cache(RecordUpdateView.as_view()), name='record_update'),
    path('record/delete/<int:pk>/', never_cache(RecordDeleteView.as_view()), name='record_delete'),
]