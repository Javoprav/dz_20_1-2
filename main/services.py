from django.core.mail import send_mail
from django.conf import settings


def send_email(record_item):  # отправка письма
    send_mail(
        '100 просмотров',
        '100 просмотров! Ура! Теперь надо 1000',
        settings.EMAIL_HOST_USER,
        ['javoprav@gmail.com']
        # [user.email]
    )