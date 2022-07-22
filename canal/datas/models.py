from django.db import models


class Order(models.Model):
    """Данные о заказах."""

    order_id = models.IntegerField('ID объекта из файла', unique=True)
    number = models.IntegerField('Номер заказа')
    cost_dollar = models.FloatField('Стоимость в долларах')
    cost_ruble = models.FloatField('Стоимость в рублях')
    date = models.DateField('Cрок поставки')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['order_id']

    def __str__(self):
        return str(self.number)
