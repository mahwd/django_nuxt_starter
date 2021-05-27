from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="Email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="Date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Last login", auto_now=True)
    is_admin = models.DateTimeField(default=False)
    is_active = models.DateTimeField(default=True)
    is_staff = models.DateTimeField(default=False)
    is_superuser = models.DateTimeField(default=False)

    USERNAME_FIELD = 'email'
