from django.contrib import admin

from server.apps.parser.models import ProductsModel, SessionParsingModel


@admin.register(ProductsModel)
class ProductsModelAdmin(admin.ModelAdmin):
    """Admin panel ``ProductsModel`` model."""
    list_display = ('id', 'name', 'url', 'price', 'session_parsing')


@admin.register(SessionParsingModel)
class ProductsModelAdmin(admin.ModelAdmin):
    """Admin panel ``SessionParsingModel`` model."""
    list_display = ('datetime_parse',)

