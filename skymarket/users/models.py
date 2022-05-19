from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser):
    # TODO переопределение пользователя.
    USERNAME_FIELD = 'email'
    USER = 'user'
    ADMIN = 'admin'
    ROLES = [
        ("user", "Пользователь"),
        ("admin", "Админ")
    ]

    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    objects = UserManager()

    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER


class UserRoles(models.Model):
    USER = 'user'
    ADMIN = 'admin'
    ROLES = [
        ("user", "Пользователь"),
        ("admin", "Админ")
    ]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.CharField(User.USERNAME_FIELD, max_length=10)
    role = models.CharField(max_length=9, choices=ROLES, default="user")
    image = models.ImageField(upload_to='ads/', null=True, blank=True)
