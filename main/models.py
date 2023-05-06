from django.db import models
NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(max_length=15000, verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='image/', verbose_name='Изображение', **NULLABLE)
    # category = models.CharField(max_length=150, verbose_name='Категория')
    category = models.ForeignKey(verbose_name='Категория', to='Category', on_delete=models.PROTECT)
    price_for_pickup = models.IntegerField(verbose_name='Цена за покупку')
    date_of_creation = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    last_modified_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name}, {self.category}, {self.price_for_pickup}, {self.date_of_creation}, {self.last_modified_date}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('name', 'category', 'price_for_pickup', 'date_of_creation')


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(max_length=15000, verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}, {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)