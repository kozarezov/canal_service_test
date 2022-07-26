# Generated by Django 3.2.14 on 2022-07-25 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datas', '0002_change_id_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cost_dollar',
            field=models.FloatField(null=True, verbose_name='Стоимость в долларах'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cost_ruble',
            field=models.FloatField(null=True, verbose_name='Стоимость в рублях'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(null=True, verbose_name='Cрок поставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='number',
            field=models.IntegerField(null=True, verbose_name='Номер заказа'),
        ),
    ]
