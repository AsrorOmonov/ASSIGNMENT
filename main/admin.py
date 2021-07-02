from django.contrib import admin

from main.models import UserModel


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'salary', 'created_at']
    list_filter = ['name', 'age', 'salary']
