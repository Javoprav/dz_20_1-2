from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView

from main.models import Product


class IndexView(TemplateView):
    template_name = 'main/index.html'
    extra_context = {
        'title': 'Главная страница',
        'object_list': Product.objects.all()
    }


class ProductListView(ListView):  # выведение контекста студентов из модели по ключу object_list
    model = Product
    extra_context = {
        'object_list': Product.objects.all(),
        'title': 'Все продукты'  # дополнение к статической информации
    }


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_object()
        return context_data


class ContactView(TemplateView):
    template_name = 'main/contact.html'
    extra_context = {
        'title': 'Контакты'
    }

    def get_context_data(self, **kwargs):
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            email = self.request.POST.get('email')
            message = self.request.POST.get('message')
            print(f'You have new message from {name}({email}): {message}')
        return super().get_context_data(**kwargs)

# def contacts(request):  # в файле request хранится вся инфа от пользователя
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         print(f'name {name}, email {email}, message {message}')
#
#     context = {
#         'title': 'Контакты'
#     }
#     return render(request, 'main/contact.html', context)  # шаблон main/contact.html


# def index(request):
#     # ШАБЛОННЫЕ ПЕРЕМЕННЫЕ
#     context = {
#         'object_list': Product.objects.all(),   # выведение контекста студентов из модели по ключу object_list
#         'title': 'Главная'
#     }
#     return render(request, 'main/index.html', context)

# def products(request):
#     # ШАБЛОННЫЕ ПЕРЕМЕННЫЕ
#     context = {
#         'object_list': Product.objects.all(),
#         'title': 'Все товары'
#     }
#     return render(request, 'main/product_list.html', context)

# def product(request, pk):
#     product_item = Product.objects.get(pk=pk)
#     context = {
#         'objects': product_item,
#         'title': product_item,
#     }
#     return render(request, 'main/product_detail.html', context)