from django.contrib import admin
from users.models.user import CustomUser
# Register your models here.
admin.site.register(CustomUser)