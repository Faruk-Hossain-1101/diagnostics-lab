from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Custom manager for the User model to handle user and superuser creation.
    """
    def create_user(self, phone, first_name, last_name, password=None, **extra_fields):
        """
        Create and return a regular user with the given email, first name, last name, and password.
        """
        if not phone:
            raise ValueError("The Phone field must be set")
        
        user = self.model(
            phone=phone,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, first_name, last_name, password=None, **extra_fields):
        """
        Create and return a superuser with the given email, first name, last name, and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser=True.")
        
        return self.create_user(phone, first_name, last_name, password, **extra_fields)
