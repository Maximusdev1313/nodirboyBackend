from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Filial)
admin.site.register(Day)
admin.site.register(TotalProducts)
admin.site.register(SoldProducts)
admin.site.register(ReportByProduct)
admin.site.register(EntryProducts)
admin.site.register(Product)
admin.site.register(ReturnProducts)
admin.site.register(ReturnedProduct)
