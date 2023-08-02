from django.contrib import admin

from server.apps.parser.models import ProductsModel


@admin.register(ProductsModel)
class ProductsModelAdmin(admin.ModelAdmin):
    """Admin panel ``ProductsModel`` model."""
    list_display = ('id', 'name', 'url', 'price', 'datetime_parse')
