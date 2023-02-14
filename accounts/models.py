from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=127, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField(null=True)
    is_employee = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_employee:
            self.is_superuser = True
        else:
            self.is_superuser = False
        super().save(*args, **kwargs)
