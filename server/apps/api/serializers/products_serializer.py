from rest_framework import serializers

from server.apps.parser.models import ProductsModel


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductsModel
        fields = [
            'id',
            'name',
            'url',
            'price',
            'datetime_parse',
        ]
