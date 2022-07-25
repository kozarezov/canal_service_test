from pprint import pprint
from django.shortcuts import render
from django.db.models import Sum

from .models import Order
from .api import script


def index(request):
    """Главная страница с данными."""
    script()
    orders = Order.objects.all()
    sum = Order.objects.aggregate(Sum('cost_dollar'))
    context = {
        'orders': orders[:13],
        'sum': sum
    }

    return render(request, 'datas/index.html', context)
