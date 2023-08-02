from django.db import models
from django.utils import timezone


class ProductsModel(models.Model):
    name = models.CharField(
        verbose_name='Название карточки товара',
        max_length=255,
    )

    url = models.URLField(
        verbose_name='Ссылка на карточку товара',
    )

    price = models.FloatField(
        verbose_name='Стоимость товара',
    )

    datetime_parse = models.DateTimeField(
        verbose_name='Дата и время парсинга',
        default=timezone.now,
    )

    class Meta(object):
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        """Return object."""
        return self.name
