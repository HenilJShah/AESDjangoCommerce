from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("staff", "Staff"),
        ("end_user", "End User"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="end_user")

    def __str__(self):
        return self.username
