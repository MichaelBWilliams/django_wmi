from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# Register your models here.

from .models import Map, Profile


class UserProfileInlineAdmin(admin.StackedInline):
    model = Profile

class MyUserAdmin(UserAdmin):
    inlines = [ UserProfileInlineAdmin ]

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)

admin.site.register(Profile)



