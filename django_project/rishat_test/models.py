from django.db import models

class Item(models.Model):
    '''Модель предмет с полями название, описание, цена, валюта'''
    CURRENCY_CHOICES = (
            ('rub','RUB'),
            ('usd','USD'),
        )

    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.FloatField(default=0, verbose_name='Цена')
    currency = models.CharField(max_length=3, default='rub', verbose_name='Валюта',
                                choices=CURRENCY_CHOICES)

    class Meta:
        verbose_name_plural = 'Вещи'
        verbose_name = 'Вещь'
