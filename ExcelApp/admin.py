from django.contrib import admin
from .models import *


class StudentAdmin(admin.ModelAdmin):
    list_display = [ "id" ,"name", "father_name", "address", "age" ]
    search_fields = ["name"]

class NewStudentAdmin(admin.ModelAdmin):
    list_display = [ "id" ,"name", "father_name", "address", "age" ]
    search_fields = ["name"]


admin.site.register(Student, StudentAdmin)
admin.site.register(NewStudent, NewStudentAdmin)
