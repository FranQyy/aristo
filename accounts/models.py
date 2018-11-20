from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False, is_admin=False, is_active=True):
        if not email:
            raise ValueError("User must has an email address")
        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.is_staff = self.is_staff
        user_obj.is_admin = self.is_admin
        user_obj.is_active = self.is_active

        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True,
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=255)
    fullname = models.CharField(max_length=255, blank=True, null=False)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
