from django.contrib import admin
from .models import Users


class UserAdmin(admin.ModelAdmin):
    display = "id","first_name","second_name","email","location",

admin.site.register(Users,UserAdmin)