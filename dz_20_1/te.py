import os

# from django.conf.global_settings import EMAIL_HOST_USER

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')

print(str(EMAIL_HOST_USER))

for x in os.environ:
        print((x, os.getenv(x)))
print(os.environ['HOME'])