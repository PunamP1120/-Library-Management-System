from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager

class AdminUserManager(UserManager):
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("username", email)  # Set username = email by default
        return super().create_user(email=email, password=password, **extra_fields)


# Custom Admin Model
class AdminUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True, default='admin')  # Keep username but make it required
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AdminUserManager()  # Use the custom manager

# Book Model
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()

    def __str__(self):
        return self.title
