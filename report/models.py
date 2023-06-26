from django.db import models

# Create your models here.
from django.db import models


class ReturnedProduct(models.Model):
    product_bar_code = models.CharField(max_length=300, blank=True, null=True)
    product_name = models.CharField(max_length=300, blank=True, null=True)
    product_size = models.CharField(max_length=300, blank=True, null=True)
    product_entry_price = models.CharField(
        max_length=300, blank=True, null=True)
    product_price = models.CharField(max_length=300, blank=True, null=True)
    product_quantity = models.CharField(max_length=300, blank=True, null=True)
    product_total_price = models.CharField(
        max_length=600, blank=True, null=True)
    products = models.ForeignKey(
        'ReturnProducts', on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.product_name


class ReturnProducts(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    totalQuantityByKilo = models.CharField(
        max_length=1000, null=True, blank=True)
    totalQuantityByAmount = models.CharField(
        max_length=1000, null=True, blank=True)
    total = models.CharField(max_length=1000, null=True, blank=True)

    returns = models.ForeignKey(
        'TotalProducts', on_delete=models.CASCADE, related_name='returns')


class Product(models.Model):
    product_bar_code = models.CharField(max_length=300, blank=True, null=True)
    product_name = models.CharField(max_length=300, blank=True, null=True)
    product_entry_price = models.CharField(
        max_length=300, blank=True, null=True)
    product_price = models.CharField(max_length=300, blank=True, null=True)
    product_size = models.CharField(max_length=300, blank=True, null=True)
    product_quantity = models.CharField(max_length=300, blank=True, null=True)
    product_total_price = models.CharField(
        max_length=600, blank=True, null=True)
    products = models.ForeignKey(
        'EntryProducts', on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.product_name


class EntryProducts(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    totalQuantityByKilo = models.CharField(
        max_length=1000, null=True, blank=True)
    totalQuantityByAmount = models.CharField(
        max_length=1000, null=True, blank=True)
    total = models.CharField(max_length=1000, null=True, blank=True)

    entries = models.ForeignKey(
        'TotalProducts', on_delete=models.CASCADE, related_name='entries')


# ---------------------------------------------
class ReportByProduct(models.Model):
    product_bar_code = models.CharField(max_length=300, blank=True, null=True)

    product_name = models.CharField(max_length=300, blank=True, null=True)
    product_entry_price = models.CharField(
        max_length=300, blank=True, null=True)
    product_price = models.CharField(max_length=300, blank=True, null=True)
    product_quantity = models.CharField(max_length=300, blank=True, null=True)
    product_size = models.CharField(max_length=300, blank=True, null=True)
    product_total_price = models.CharField(
        max_length=600, blank=True, null=True)
    products = models.ForeignKey(
        'SoldProducts', on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.product_name


class SoldProducts(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    total = models.CharField(max_length=1000, null=True, blank=True)
    totalQuantityByKilo = models.CharField(
        max_length=1000, null=True, blank=True)
    totalQuantityByAmount = models.CharField(
        max_length=1000, null=True, blank=True)

    soldProducts = models.ForeignKey(
        'TotalProducts', on_delete=models.CASCADE, related_name='soldProducts')


class TotalProducts(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    benefit = models.CharField(
        max_length=1000, null=True, blank=True)
    totalEntriesByKilo = models.CharField(
        max_length=1000, null=True, blank=True)
    totalEntriesByAmount = models.CharField(
        max_length=1000, null=True, blank=True)
    totalOutgoingsByKilo = models.CharField(
        max_length=1000, null=True, blank=True)
    totalOutgoingsByAmount = models.CharField(
        max_length=1000, null=True, blank=True)
    totalReturnsByKilo = models.CharField(
        max_length=1000, null=True, blank=True)
    totalReturnsByAmount = models.CharField(
        max_length=1000, null=True, blank=True)
    totalProducts = models.ForeignKey(
        'Day', on_delete=models.CASCADE, related_name='totalProducts')


class Day(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    time = models.DateTimeField(auto_now_add=True, )
    day = models.ForeignKey(
        'Filial', on_delete=models.CASCADE, related_name='day')


class Filial(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


# for products -----------------------------------------------


class Products(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    bar_code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=1000, null=True, blank=True)
    quantity_in_store = models.CharField(
        max_length=1000, default=0, null=True, blank=True)
    quantity = models.CharField(
        max_length=1000, default=0, null=True, blank=True)
    entry_price = models.CharField(
        max_length=1000, default=0, null=True, blank=True)
    price = models.CharField(max_length=100, null=True, blank=True)
    is_important = models.BooleanField(default=False)
    size = models.CharField(max_length=100, null=True, blank=True)
    old_price = models.CharField(max_length=64, null=True, blank=True)
    discount = models.CharField(max_length=10, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True, )
    product = models.ForeignKey(
        'Category', on_delete=models.CASCADE, related_name='product')

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image_link = models.CharField(max_length=2000, null=True, blank=True)
    image = models.ImageField(upload_to="media", null=True, blank=True)
    title = models.CharField(max_length=2500, null=True)
    images = models.ForeignKey(
        'Products', on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.title


class Category(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class CategoryImage(models.Model):
    image_link = models.CharField(max_length=2000, null=True, blank=True)
    image = models.ImageField(upload_to="media", null=True, blank=True)
    title = models.CharField(max_length=2500, null=True)
    images = models.ForeignKey(
        'Category', on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.title


class UploadAudioTest(models.Model):
    name = models.CharField(max_length=100)
    audio = models.FileField(upload_to='media', blank=True, null=True)
