from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100, default='sample_passwd')
    email = models.EmailField(default='')

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=400)
    content = models.TextField()
    date = models.DateField()
    author = models.ForeignKey('User', default=None)

    def __str__(self):
        return self.title
