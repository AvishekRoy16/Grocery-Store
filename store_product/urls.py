from django.urls import path
from . import views 

urlpatterns = [
    path('',views.store_product,name='store_product'),
    path('<slug:category_slug>/',views.store_product,name='product_by_category'),
    path('<slug:category_slug>/<slug:product_slug>',views.product_detail,name='product_detail')
]
