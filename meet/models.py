from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=20)
    region = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Profile(AbstractUser):
    REQUIRED_FIELDS = ['email']
    photo = models.ImageField(default='no_photo.jpg')
    dob = models.DateField('Date of Birth', null=True)
    name = models.CharField(max_length=40, null=True)
    gender = models.CharField(max_length=1, null=True)
    city = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=15, null=True)
    stars = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name


class UserLanguage(models.Model):
    language = models.ForeignKey(Language, related_name='user_languages')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='languages')
    proficiency = models.IntegerField(null=False)

    def __str__(self):
        return self.language.name


class Match(models.Model):
    users = models.ManyToManyField(Profile, related_name='matches')
    date = models.DateTimeField('match timestamp')


class Unmatch(models.Model):
    users = models.ManyToManyField(Profile, related_name='unmatches')
    date = models.DateTimeField('unmatch timestamp')


class Comment(models.Model):
    match = models.ForeignKey(Match, related_name='comments')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateTimeField('comment timestamp')
    text = models.CharField(max_length=500)

    class Meta:
        ordering = ['-date', ]

