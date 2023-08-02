from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from server.apps.parser.models import ProductsModel


class ProductsSerializer(serializers.ModelSerializer):
    datetime_parse = SerializerMethodField()

    def get_datetime_parse(self, obj):
        """Дата и время парсинга из сессии."""
        return obj.session_parsing.datetime_parse

    class Meta:
        model = ProductsModel
        fields = [
            'id',
            'name',
            'url',
            'price',
            'datetime_parse',
        ]
