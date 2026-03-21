from django.contrib import admin
from .models import ReportLog

@admin.register(ReportLog)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('report_type', 'generated_at', 'file')
    list_filter = ('report_type',)