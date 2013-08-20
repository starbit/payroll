from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from users.models import UserProfile

class UserProfileInline(admin.TabularInline):
    model = UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

class CustomUserAdmin(UserAdmin):
    inlines = [UserProfileInline, ]

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
