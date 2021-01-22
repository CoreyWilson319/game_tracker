from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


# class My_Custom_User_Manager(BaseUserManager):
#     def create_user(self, email, username, password=None):
#         if not email:
#             raise ValueError("Users must have an email address")
#         if not username:
#             raise ValueError("Users must have an username")

#         user = self.model(
#             email=self.normalize_email(email),
#             username=username,
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, username, password):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             username=username,
#             password=password
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user

# class Custom_User(AbstractBaseUser):
#     email = models.EmailField(verbose_name="email", max_length=60, unique=True)
#     username = models.CharField(max_length=30, unique=True)
#     date_joined = models.DateField(
#         verbose_name='date joined', auto_now_add=True)
#     last_login = models.DateField(verbose_name='last login', auto_now=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     objects = My_Custom_User_Manager

#     def __str__(self):
#         return self.email, self.username, self.last_login, self.date_joined

#     def has_perm(self, perm, obj=None):
#         return self.is_admin

#     def has_module_perms(self, app_label):
#         return True


class Game(models.Model):
    title = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=250)
    guid = models.CharField(max_length=15)
    platforms = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    release_date = models.CharField(max_length=20)
    url = models.CharField(max_length=50)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.title, self.image, self.description, self.platforms
