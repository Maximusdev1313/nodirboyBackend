from django.urls import path, include
from .views import *
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('filial', FilialViewSet)
router.register('day', DayViewSet)
router.register('total-products', TotalProductsViewSet)
router.register('sold-products', SoldProductsViewSet)
router.register('report-by-product-sold', ReportByProductViewSet)

router.register('entry', EntryProductsViewSet)
router.register('entry-products', ProductViewSet)

router.register('return-products', ReturnProductsViewSet)
router.register('returned-product', ReturnedProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # url(r'^users/(?P<username>[a-zA-Z0-9]+)$', CategoryViewSet.as_view({'get': 'retrieve'})),
    # path('/simple/', include(router.urls) )
]
