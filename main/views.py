from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from main.forms import ProductForm, VersionForm
from main.services import send_email, get_category_subjects
from main.models import Product, Record, Version, Category


class IndexView(TemplateView):
    template_name = 'main/index.html'
    extra_context = {
        'title': 'Главная страница',
        'object_list': Product.objects.filter(status='Активна')
    }


class CategoriesListView(ListView):
    model = Category
    extra_context = {
        'title': 'Все категории',
        'object_list': Category.objects.all()
    }

    def get_context_data(self, **kwargs):   # меняет title на __str__.object (имя студента)
        context_data = super().get_context_data(**kwargs)
        context_data['subject_list'] = get_category_subjects    # логика вынесена в services.py ---------
        return context_data


class ProductListView(ListView):  # выведение контекста студентов из модели по ключу object_list
    model = Product
    extra_context = {
        'object_list': Product.objects.filter(status='Активна'),
        'version_list': Version.objects.filter(sign_of_publication=True),
        'title': 'Все продукты'  # дополнение к статической информации
    }


class RecordListView(ListView):  # выведение контекста записей из модели по ключу object_list
    model = Record
    extra_context = {
        # 'object_list': Record.objects.all(),
        'title': 'Все записи',  # дополнение к статической информации
    }

    def get_queryset(self):  # выводит только активные записи
        queryset = super().get_queryset()
        queryset = queryset.filter(sign_of_publication=True)
        return queryset


class RecordDetailView(DetailView):
    model = Record

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_object()
        obj = self.get_object()
        increase = get_object_or_404(Record, pk=obj.pk)  # увеличение количества просмотров
        increase.increase_views()
        if increase.views == 100:
            send_email(increase)  # отправка письма
        return context_data


class RecordCreateView(CreateView):
    model = Record
    fields = ('record_title', 'slug', 'content', 'preview')
    success_url = reverse_lazy('main:records_list')


class RecordUpdateView(UpdateView):
    model = Record
    fields = ('record_title', 'slug', 'content', 'preview',)

    def get_success_url(self):
        return reverse('main:record_detail', args=[str(self.object.slug)])

    def get_object(self, queryset=None):     # продукт должен редактировать только владелец
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404("Вы не являетесь владельцем этого товара")
        return self.object


class RecordDeleteView(DeleteView):
    model = Record
    success_url = reverse_lazy('main:records_list')


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_object()
        return context_data


class ProductCreateView(LoginRequiredMixin, CreateView):  # LoginRequiredMixin требует авторизацию
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:products_list')

    def form_valid(self, form):           # добавление создателя
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form_with_formset.html'
    success_url = reverse_lazy('main:products_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)  # extra= 2 выведет 2 формы
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST)  # instance=self.object выводит ещё одну форму
        else:
            context_data['formset'] = SubjectFormset()
        return context_data


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('main:products_list')


class VersionListView(ListView):
    """# выведение контекста версий из модели по ключу object_list"""
    model = Version
    extra_context = {
        'object_list': Version.objects.filter(sign_of_publication=True),
        'title': 'Все версии'
    }


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('main:products_list')


class VersionDetailView(DetailView):
    model = Version

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
        """Получение данных из формы"""
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        if not name or not email or not message:
            context = {"error": "Введите все поля!"}
            return render(request, self.template_name, context=context)

        print(f'Сообщение от {name}({email}): {message}')

        context = {"success": "Сообщение успешно отправлено!"}
        return render(request, self.template_name, context=context)
