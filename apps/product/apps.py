from django.apps import AppConfig


class Product(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.product'
    verbose_name = 'Продукты'
