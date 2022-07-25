import json
from django.shortcuts import render
from django.db.models import Sum

from .models import Order
from .api import script


def querySet_to_list(result):
    """Переделываем QuerySet в List."""
    array = []
    for res in result:
        for key, value in res.items():
            array.append(value)
    return array


def chart_data():
    """Функция необходимая для сбора данных в графике."""
    dates = querySet_to_list(Order.objects.values('date').distinct())
    sums = []
    dates_array = []

    for date in dates:
        date_sum = (
            Order.objects.
            filter(date=date).
            aggregate(Sum('cost_dollar')).
            get('cost_dollar__sum')
        )
        sums.append(date_sum)
        dates_array.append(date.strftime("%d.%m.%Y"))

    return sums, dates_array


def index(request):
    """Главная страница с данными."""
    script()
    orders = Order.objects.all()
    sum = orders.aggregate(Sum('cost_dollar'))
    chart_sums, chart_date = chart_data()
    context = {
        'orders': orders[:13],
        'sum': sum,
        'chart_sums': json.dumps(chart_sums),
        'chart_date': json.dumps(chart_date),
    }

    return render(request, 'datas/index.html', context)
