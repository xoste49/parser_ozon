from django.urls import include, path
from rest_framework import routers
from server.apps.api.views import ProductsViewSet

router = routers.SimpleRouter()
router.register('products', ProductsViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),
]
