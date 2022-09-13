from django.contrib.auth.password_validation import validate_password
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    username = models.CharField(max_length=100, unique=True, default=None, null=True)
    password = models.CharField(max_length=100, null=False, blank=False)

    def set_password(self, raw_password):
        validate_password(password=raw_password, user=self)
        self.password = make_password(raw_password)

    class Meta:
        db_table = 'users'
        verbose_name_plural = "Users"
        verbose_name = "User"

    def __str__(self):
        return self.email
