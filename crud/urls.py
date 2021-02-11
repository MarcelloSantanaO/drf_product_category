from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, ProductViewSet, ProductByCategoryViewSet

router = routers.DefaultRouter()
router.register(r'Category', CategoryViewSet, basename='category')
router.register(r'Product', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('product/category/<int:id>', ProductByCategoryViewSet.as_view()),
    path('api-auth', include(
        'rest_framework.urls', namespace='rest_framework'
    ))
]
