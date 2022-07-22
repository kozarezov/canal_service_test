from pprint import pprint
from django.shortcuts import render

from .models import Order
from .api import script


def index(request):
    """Главная страница с данными."""
    script()
    orders = Order.objects.all()
    context = {
        'orders': orders,
    }

    return render(request, 'datas/index.html', context)
