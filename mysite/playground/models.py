from django.db import models
from manager import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser



# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    username = None  # Remove the username field

    USERNAME_FIELD = 'email'  # Use email for authentication
    REQUIRED_FIELDS = []  # No other fields required for superuser

    objects = CustomUserManager()

    def __str__(self):
        return self.email