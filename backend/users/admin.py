from django.contrib import admin
from users.models.user import CustomUser
from users.models.student import Student
from users.models.teatcher import Teatcher
# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
  pass

class StudentAdmin(admin.ModelAdmin):
  pass 

class TeatcherAdmin(admin.ModelAdmin):
  pass

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Teatcher, TeatcherAdmin)
admin.site.register(Student, StudentAdmin)