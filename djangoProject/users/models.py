from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"{self.id}: {self.get_full_name()}"

    class Meta:
        db_table = 'users'
