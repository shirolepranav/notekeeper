# notekeeper/accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    subscription_status = models.CharField(
        max_length=20,
        choices=[
            ('active', 'Active'),
            ('inactive', 'Inactive'),
            ('trial', 'Trial')
        ],
        default='trial'
    )

class User(AbstractUser):
    is_individual = models.BooleanField(default=True)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    subscription_status = models.CharField(
        max_length=20,
        choices=[
            ('active', 'Active'),
            ('inactive', 'Inactive'),
            ('trial', 'Trial')
        ],
        default='trial'
    )