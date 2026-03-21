from django.contrib import admin
from .models import Enrollment

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'admission_date', 'status')
    list_filter = ('status', 'course')
    search_fields = ('student__name', 'course__name')