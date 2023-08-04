from django.db import models
from django.urls import reverse

from apps.users.models import User


class Product(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=128)
    brand = models.CharField(verbose_name='Бренд', max_length=128)
    description = models.TextField(verbose_name='Описание')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='product_creator')
    price = models.DecimalField(verbose_name='Цена', decimal_places=6)
    photo = models.ImageField(verbose_name='Фото',
                            upload_to='images/', default='images/default.png',
                              )
    in_stock = models.BooleanField(verbose_name='В наличии', default=True)

    class Meta:
        verbose_name = 'Продукт',
        verbose_name_plural = 'Продукты'
        ordering = ('-created',)

    def __str__(self):
        return f'Наименование:{self.product.title}, цена: {self.product.price}'
