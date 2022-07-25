from django.db import models


class Order(models.Model):
    """Данные о заказах."""

    excel_id = models.IntegerField('ID объекта из файла', unique=True)
    number = models.IntegerField('Номер заказа', null=True)
    cost_dollar = models.FloatField('Стоимость в долларах', null=True)
    cost_ruble = models.FloatField('Стоимость в рублях', null=True)
    date = models.DateField('Cрок поставки', null=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['excel_id']

    def __str__(self):
        return str(self.number)
