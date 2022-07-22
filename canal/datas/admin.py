from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Настройки админки для модели Order."""

    list_display = ('order_id', 'number', 'cost_dollar', "cost_ruble", "date")
    search_fields = ('order_id', 'number')
    list_filter = ('order_id', 'date',)
    empty_value_display = "-пусто-"
