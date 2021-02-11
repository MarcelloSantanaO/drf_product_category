from rest_framework import viewsets
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework import generics


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductByCategoryViewSet(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        id_ = self.kwargs['id']
        return Product.objects.filter(categories=id_)
