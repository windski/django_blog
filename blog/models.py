from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class NewUser(AbstractUser):
    profile = models.CharField('profile', default='', max_length=256)

    def __str__(self):
        return str([self.username, self.password, self.email])


class Column(models.Model):
    name = models.CharField('column_name', max_length=256)
    intro = models.TextField('introduction', default='')

    def __str__(self):
        return self.name


class Article(models.Model):
    column = models.ForeignKey(Column, blank=True, null=True, verbose_name = 'belong to')
    title = models.CharField(max_length=400)
    content = models.TextField()
    date = models.DateField()
    author = models.ForeignKey('User')
    user = models.ManyToManyField('NewUser', blank=True)

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100, default='sample_passwd')
    email = models.CharField(max_length=254, default='')
    profile = models.CharField('profile', default='', max_length=256)

    def __str__(self):
        return self.name

