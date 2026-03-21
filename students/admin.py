from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('reg_no', 'name', 'email', 'mobile')
    search_fields = ('name', 'email', 'mobile', 'reg_no')