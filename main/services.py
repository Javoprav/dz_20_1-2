from django.core.mail import send_mail
from django.conf import settings
from django.core.cache import cache

from main.models import Category


def send_email(record_item):  # отправка письма
    send_mail(
        f'100 просмотров {record_item}',
        '100 просмотров накрутил! Ура! Теперь надо 1000!',
        settings.EMAIL_HOST_USER,
        ['javoprav@gmail.com'],  # [user.email]
    )


def get_category_subjects():
    queryset = Category.objects.all()
    if settings.CACHE_ENABLED:
        key = 'categories'
        cache_data = cache.get(key)
        if cache_data is None:
            cache_data = queryset
            cache.set(key, cache_data)
        return cache_data
    return queryset
