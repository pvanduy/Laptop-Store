from django.urls import path
from django.urls import path,re_path

from . import views

urlpatterns = [
    re_path(r'^products/(?P<ProductCode>.*)/$', views.renderProduct.productDetail, name='product'),
    re_path(r'^home/(?P<brandName>.*)/$', views.renderProduct.productType, name='productCollections'),
    path('addToCart', views.renderProduct.addToCart, name='addToCart'),
    path('DeleteCartItem/<str:ProductCode>', views.renderProduct.DeleteCartItem, name='DeleteCartItem'),
]
