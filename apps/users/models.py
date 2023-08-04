from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.users.managers import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from rest_framework.authtoken.models import Token
from django.utils import timezone


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(verbose_name='Имя', max_length=128)
    last_name = models.CharField(verbose_name='Фамилия', max_length=128)
    email = models.CharField(verbose_name='Почта', unique=True, max_length=208 )
    is_active = models.BooleanField(verbose_name='Активный', default=True)
    is_staff = models.BooleanField(verbose_name='Сотрудник', default=False)
    date_joined = models.DateTimeField(verbose_name='Зарегистрирован', default=timezone.now)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 't_users'

    def __str__(self):
        return f'{self.email}'


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None,created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)