from typing import List

from django.contrib.auth.models import AbstractUser
from django.db import models

from authentication.managers import UserManager


class User(AbstractUser):
    objects = UserManager()

    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: List[str] = []
