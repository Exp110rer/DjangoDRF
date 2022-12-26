from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUsers(AbstractUser):
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
