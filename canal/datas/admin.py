from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Настройки админки для модели Order."""

    list_display = ('excel_id', 'number', 'cost_dollar', "cost_ruble", "date")
    search_fields = ('excel_id', 'number')
    list_filter = ('excel_id', 'date',)
    empty_value_display = "-пусто-"
