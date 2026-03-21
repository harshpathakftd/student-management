from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'amount', 'due_date', 'paid')
    list_filter = ('paid', 'due_date')
    search_fields = ('enrollment__student__name',)