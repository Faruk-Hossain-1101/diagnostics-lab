from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from accounts.manager import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('Doctor', 'Doctor'),
        ('Technician', 'Technician'),
        ('Admin', 'Admin'),
        ('Staff', 'Staff'),
        ('User', 'User'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    address = models.TextField()

    # These fields are already part of Django's authentication system
    is_staff = models.BooleanField(default=False)  
    is_superuser = models.BooleanField(default=False)  
    is_active = models.BooleanField(default=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role']  # Specify required fields other than USERNAME_FIELD


    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role}"
