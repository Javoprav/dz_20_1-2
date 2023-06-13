from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm, PasswordResetForm, \
    SetPasswordForm
from django import forms
from main.forms import FormStyleMixin
from users.models import User


class UserForm(FormStyleMixin, UserChangeForm):  # форма изменения данных пользователя
    class Meta:
        model = User
        fields = ('email', 'phone', 'avatar', 'first_name', 'last_name', 'country',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # print(self.fields['password'])
        self.fields['password'].widget = forms.HiddenInput()  # скрывает password при заполнении


class UserRegisterForm(FormStyleMixin, UserCreationForm):  # форма регистрации
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'country',)


class CustomPasswordChangeForm(FormStyleMixin, PasswordChangeForm):
    pass


class CustomPasswordResetForm(FormStyleMixin, PasswordResetForm):
    pass


class CustomSetPasswordForm(FormStyleMixin, SetPasswordForm):
    pass