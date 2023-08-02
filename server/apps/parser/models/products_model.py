from django.db import models


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

    session_parsing = models.ForeignKey(
        'parser.SessionParsingModel',
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Сессия парсинга',
    )

    class Meta(object):
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        """Return object."""
        return self.name
