from django.contrib import admin
from main.models import Product, Category, Record, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price_for_pickup', 'category',)
    list_filter = ('name',)
    search_fields = ('name', 'description')


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'record_title',)
    list_filter = ('record_title',)
    search_fields = ('record_title',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'number', 'name', 'sign_of_publication',)
    list_filter = ('sign_of_publication', 'product')
    search_fields = ('product',)