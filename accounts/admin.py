from django.contrib import admin

from accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ["phone", "email", "full_name"]
