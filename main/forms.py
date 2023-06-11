from django import forms

import dz_20_1.settings
from main.models import Product, Record, Version


class FormStyleMixin:  # стилизация формы
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(FormStyleMixin, forms.ModelForm):  # импорт форм в views.py

    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('', '')
        # exclude = ('is_active', )  # исключает поле из формы

    def clean_name(self):    # валидация на слова
        cleaned_data = self.cleaned_data['name']
        for word in dz_20_1.settings.STOP_WORDS:
            if word in cleaned_data:
                raise forms.ValidationError(f'Запрещенная тематика "{word}"')
        return cleaned_data

    # def clean_first_name(self):                              # валидация на имя
    #     cleaned_data = self.cleaned_data.get('fist_name')
    #
    #     if ...:
    #         raise forms.ValidationError('Ошибка, связанная с именем пользователя')
    #
    #     return cleaned_data


class VersionForm(FormStyleMixin, forms.ModelForm):  # импорт форм в views.py

    class Meta:
        model = Version
        fields = '__all__'
        exclude = ('sign_of_publication',)  # исключает поле из формы