from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, status
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from server.apps.api.serializers import ProductsSerializer
from server.apps.parser.models import ProductsModel
from server.apps.parser.tasks import parse_products_seller_task

@method_decorator(
    name='list',
    decorator=swagger_auto_schema(
        operation_summary='Список товаров',
        operation_description='Список товаров и информация о каждом товаре из базы.'
    ),
)
@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        operation_summary='Информация о товаре',
        operation_description='Информация о товаре из базы.'
    ),
)
class ProductsViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    """View для получения товаров и запуска парсинга."""

    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return ProductsModel.objects.all()

    def get_serializer_class(self):
        return ProductsSerializer

    @swagger_auto_schema(
        responses={
            201: openapi.Response(
                'Парсинг запущен',
                examples={
                    'application/json': [
                        {
                            'products_count': 'integer',
                        },
                    ],
                },
            ),
            400: openapi.Response('Ошибка в переданных параметрах'),
        },
        operation_summary='Запуск парсинга',
    )
    @action(methods=['post'], detail=False)
    def post(self, request):
        """Запустить задачу на парсинг"""
        data = dict(request.data)
        products_count: int = data.get('products_count', 10)
        if not isinstance(products_count, int):
            return Response(
                {'error': 'products_count должен быть числом'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if products_count > 50:
            return Response(
                {'error': 'products_count должен быть не больше 50'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        parse_products_seller_task.delay(products_count)
        return Response(status=status.HTTP_201_CREATED)
