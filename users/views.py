from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView

from users.forms import UserForm, UserRegisterForm
from users.models import User


class ProfileUpdateView(UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    # def form_valid(self, form):
    #     # Метод, который отрабатывает при успешной валидации формы
    #     if form.is_valid():
    #         self.object = form.save()
    #         # Сохранение объекта перед тем, как установить ему пароль
    #         if form.data.get('need_generate', False):
    #             self.object.set_passeword(  # Функция установки пароля,
    #                 # которая хеширует строку для того, чтобы не хранить пароль в открытом виде в БД
    #                 self.object.make_random_password(12)  # Функция генерации пароля
    #             )
    #             self.object.save()
    #     return super().form_valid(form)


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('main:index')
