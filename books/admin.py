from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AdminUser, Book

# Register your models here.
admin.site.register(AdminUser, UserAdmin)
admin.site.register(Book)