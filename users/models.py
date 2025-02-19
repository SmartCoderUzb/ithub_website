from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, tel, password=None, **extra_fields):
        if not tel:
            raise ValueError("The Tel field must be set")
        tel = tel
        user = self.model(tel=tel, **extra_fields)
        print(password)
        user.set_password(password)
        print(user.password)
        user.save(using=self._db)
        return user

    def create_superuser(self, tel, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(tel, password, **extra_fields)
    
class User(AbstractBaseUser):
    first_name = None
    last_name = None
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    t_yil = models.DateField()
    tel = models.CharField(max_length=100, unique=True)

    USERNAME_FIELD = "tel"
    REQUIRED_FIELDS = ["ism","familiya","t_yil"]

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, perm, obj=None):
        return True
    
    def save(self, *args, **kwargs):
        if self._state.adding and self.password and not self.password.startswith('pbkdf2_sha256$'):
            self.set_password(self.password)  # ✅ Hash password if not already hashed
        super().save(*args, **kwargs)