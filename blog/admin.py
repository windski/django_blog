from django.contrib import admin
from .models import User, Article

# Register your models here.

class userAdmin(admin.ModelAdmin):
    fields = ['name', 'password', 'email']

class articleAdmin(admin.ModelAdmin):
    fieldsets = [
            ('Something..', {'fields': ['title']}),
            (None,          {'fields': ['content']}),
            ('Lalala',      {'fields': ['author']}),
            ('Latest',      {'fields': ['date']}),
    ]

admin.site.register(User, userAdmin)
admin.site.register(Article, articleAdmin)

