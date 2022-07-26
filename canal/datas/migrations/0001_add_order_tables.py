# Generated by Django 3.2.14 on 2022-07-22 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(unique=True, verbose_name='ID объекта из файла')),
                ('number', models.IntegerField(verbose_name='Номер заказа')),
                ('cost_dollar', models.FloatField(verbose_name='Стоимость в долларах')),
                ('cost_ruble', models.FloatField(verbose_name='Стоимость в рублях')),
                ('date', models.DateField(verbose_name='Cрок поставки')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['order_id'],
            },
        ),
    ]
