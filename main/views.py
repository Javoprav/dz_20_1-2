from django.shortcuts import render

from main.models import Product


def index(request):
    # ШАБЛОННЫЕ ПЕРЕМЕННЫЕ
    context = {
        'object_list': Product.objects.all(),   # выведение контекста студентов из модели по ключу object_list
        'title': 'Главная'
    }
    return render(request, 'main/index.html', context)


def products(request):
    # ШАБЛОННЫЕ ПЕРЕМЕННЫЕ
    context = {
        'object_list': Product.objects.all(),
        'title': 'Все товары'
    }
    return render(request, 'main/products.html', context)


def product(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'objects': product_item,
        'title': product_item,
    }
    return render(request, 'main/product.html', context)


def contacts(request):  # в файле request хранится вся инфа от пользователя
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'name {name}, email {email}, message {message}')

    context = {
        'title': 'Контакты'
    }
    return render(request, 'main/contact.html', context)  # шаблон main/contact.html