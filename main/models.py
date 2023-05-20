from django.db import models
from django.urls import reverse

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(max_length=15000, verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='image/', verbose_name='Изображение', **NULLABLE)
    # category = models.CharField(max_length=150, verbose_name='Категория')
    category = models.ForeignKey(verbose_name='Категория', to='Category', on_delete=models.CASCADE)
    price_for_pickup = models.IntegerField(verbose_name='Цена за покупку')
    date_of_creation = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    last_modified_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name}' #, {self.category}, {self.price_for_pickup}, {self.date_of_creation}, {self.last_modified_date}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('name', 'category', 'price_for_pickup', 'date_of_creation')


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(max_length=15000, verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Record(models.Model):
    record_title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(max_length=15000, verbose_name='Содержимое')
    preview = models.ImageField(upload_to='image/', verbose_name='Изображение', **NULLABLE)
    date_of_creation = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    sign_of_publication = models.BooleanField(default=True, verbose_name='активный')
    # number_of_views =

    def __str__(self):
        return f'{self.record_title}'

    def get_absolute_url(self):
        return reverse('record_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
        ordering = ('record_title', 'slug', 'date_of_creation', 'sign_of_publication')