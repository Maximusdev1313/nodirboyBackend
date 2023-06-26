from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


class ReturnedProductViewSet(ModelViewSet):
    queryset = ReturnedProduct.objects.all()
    serializer_class = ReturnedProductSerializer


class ReturnProductsViewSet(ModelViewSet):
    queryset = ReturnProducts.objects.all()
    serializer_class = ReturnProductsSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class EntryProductsViewSet(ModelViewSet):
    queryset = EntryProducts.objects.all()
    serializer_class = EntryProductsSerializer


class ReportByProductViewSet(ModelViewSet):
    queryset = ReportByProduct.objects.all()
    serializer_class = ReportByProductSerializer


class SoldProductsViewSet(ModelViewSet):
    queryset = SoldProducts.objects.all()
    serializer_class = SoldProductsSerializer


class TotalProductsViewSet(ModelViewSet):
    queryset = TotalProducts.objects.all()
    serializer_class = TotalProductsSerializer


class DayViewSet(ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer


class FilialViewSet(ModelViewSet):
    queryset = Filial.objects.all()
    serializer_class = FilialSerializer


#  for products  ----------------------------------------------

class UploadAudioTestViewSet(ModelViewSet):
    queryset = UploadAudioTest.objects.all()
    serializer_class = UploadAudioTestSerializer


class ProductViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class ProductImageViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryImageViewSet(ModelViewSet):
    queryset = CategoryImage.objects.all()
    serializer_class = CategoryImageSerializer
