from django.contrib import admin
from .models import User, Article, NewUser, Column

# Register your models here.

class userAdmin(admin.ModelAdmin):
    fields = ['name', 'password', 'profile']

class articleAdmin(admin.ModelAdmin):
    fieldsets = [
            ('Something..', {'fields': ['title']}),
            (None,          {'fields': ['content']}),
            ('Lalala',      {'fields': ['author']}),
            ('Latest',      {'fields': ['date']}),
    ]


class newuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'date_joined', 'profile')


class columnAdmin(admin.ModelAdmin):
    list_display = ('name', 'intro')

admin.site.register(Article, articleAdmin)
admin.site.register(NewUser, newuserAdmin)
admin.site.register(Column, columnAdmin)
admin.site.register(User, userAdmin)

