from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    game_title = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.user, self.created_at, self.content, self.game_title


class Game(models.Model):
    title = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    guid = models.CharField(max_length=15)
    platforms = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    release_date = models.CharField(max_length=20)
    url = models.CharField(max_length=50)
    users = models.ManyToManyField(User)
    notes = models.ManyToManyField(Note)

    def __str__(self):
        return self.title, self.image, self.description, self.platforms, self.notes


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Game)
# Notes
# Notes have users
# Notes could take game information based on if the Game has a user of the current user
