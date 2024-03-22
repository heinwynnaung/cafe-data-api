from django.urls import path
from .views import StoreDetailUpdateDelete, StoreList
from .views import ProductDetailUpdateDelete, ProductList

urlpatterns = [
    path('stores/', StoreList.as_view(), name='store_list'),
    path('stores/<int:store_id>/',
         StoreDetailUpdateDelete.as_view(), name='store_detail'),

    path('products/', ProductList.as_view(), name='product_list'),
    path('products/<int:product_id>/',
         ProductDetailUpdateDelete.as_view(), name='product_detail'),
]
