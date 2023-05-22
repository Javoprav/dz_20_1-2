from django.core.mail import send_mail
from django.conf import settings


def send_email(record_item):  # отправка письма
    send_mail(
        f'100 просмотров {record_item}',
        '100 просмотров накрутил! Ура! Теперь надо 1000!',
        settings.EMAIL_HOST_USER,
        ['javoprav@gmail.com'],  # [user.email]
    )
