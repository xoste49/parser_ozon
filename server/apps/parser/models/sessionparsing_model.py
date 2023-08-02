from django.db import models
from django.utils import timezone


class SessionParsingModel(models.Model):
    """Сессия парсинга."""
    datetime_parse = models.DateTimeField(
        verbose_name='Дата и время парсинга',
        default=timezone.now,
    )

    class Meta(object):
        verbose_name = 'Сессия парсинга'
        verbose_name_plural = 'Сессии парсинга'

    def __str__(self):
        """Return object."""
        return str(self.datetime_parse)
