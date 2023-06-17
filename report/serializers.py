from rest_framework import serializers
from .models import *


class ReturnedProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReturnedProduct
        fields = ['id', 'product_bar_code', 'product_name', 'product_price',
                  'product_quantity', 'product_size', 'product_total_price', 'products']


class ReturnProductsSerializer(serializers.ModelSerializer):
    products = ReturnedProductSerializer(many=True, read_only=True)

    class Meta:
        model = ReturnProducts
        fields = ['id', 'totalQuantityByKilo',
                  'totalQuantityByAmount', 'total', 'products', 'returns']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'product_bar_code', 'product_name', 'product_price',
                  'product_quantity', 'product_size', 'product_total_price', 'products']


class EntryProductsSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = EntryProducts
        fields = ['id', 'totalQuantityByKilo',
                  'totalQuantityByAmount', 'total', 'products', 'entries']

# ---------------------------------------------------------------


class ReportByProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReportByProduct
        fields = ['id', 'product_bar_code', 'product_name', 'product_price',
                  'product_quantity', 'product_size', 'product_total_price', 'products']


class SoldProductsSerializer(serializers.ModelSerializer):
    products = ReportByProductSerializer(many=True, read_only=True)

    class Meta:
        model = SoldProducts
        fields = ['id', 'totalQuantityByKilo',
                  'totalQuantityByAmount', 'total', 'soldProducts', 'products']
# ------------------------------
# -------------------


class TotalProductsSerializer(serializers.ModelSerializer):
    soldProducts = SoldProductsSerializer(many=True, read_only=True)
    entries = EntryProductsSerializer(many=True, read_only=True)
    returns = ReturnProductsSerializer(many=True, read_only=True)

    class Meta:
        model = TotalProducts
        fields = ['id', 'benefit', 'totalEntriesByKilo', 'totalEntriesByAmount', 'totalOutgoingsByKilo', 'totalOutgoingsByAmount', 'totalReturnsByKilo', 'totalReturnsByAmount',
                  'totalProducts', 'soldProducts', 'entries', 'returns']


class DaySerializer(serializers.ModelSerializer):
    totalProducts = TotalProductsSerializer(many=True, read_only=True)

    class Meta:
        model = Day
        fields = ['id', 'time', 'day', 'totalProducts']


class FilialSerializer(serializers.ModelSerializer):
    day = DaySerializer(many=True, read_only=True)

    class Meta:
        model = Filial
        fields = ['id', 'name', 'address', 'day', ]
