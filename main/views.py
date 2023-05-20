from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView

from main.models import Product, Record


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


class RecordListView(ListView):  # выведение контекста студентов из модели по ключу object_list
    model = Record
    extra_context = {
        'object_list': Record.objects.all(),
        'title': 'Все записи'  # дополнение к статической информации
    }


class RecordDetailView(DetailView):
    model = Record

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_object()
        obj = self.get_object()
        increase = get_object_or_404(Record, pk=obj.pk)  # увеличение количества просмотров
        increase.increase_views()
        return context_data


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

    def post(self, request, *args, **kwargs):
        # получение данных из формы
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        if not name or not email or not message:
            context = {"error": "Введите все поля!"}
            return render(request, self.template_name, context=context)

        print(f'Сообщение от {name}({email}): {message}')

        context = {"success": "Сообщение успешно отправлено!"}
        return render(request, self.template_name, context=context)


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

# class ContactView(TemplateView):
#     template_name = 'main/contact.html'
#     extra_context = {
#         'title': 'Контакты'
#     }
#
#     def get_context_data(self, **kwargs):
#         if self.request.method == 'POST':
#             name = self.request.POST.get('name')
#             email = self.request.POST.get('email')
#             message = self.request.POST.get('message')
#             print(f'You have new message from {name}({email}): {message}')
#         return super().get_context_data(**kwargs)