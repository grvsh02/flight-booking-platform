from django.contrib.auth.password_validation import validate_password
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    class Meta:
        db_table = 'users'
        verbose_name_plural = "Users"
        verbose_name = "User"

    def __str__(self):
        return self.email
