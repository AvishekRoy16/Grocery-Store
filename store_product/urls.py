from django.urls import path
from . import views 

urlpatterns = [
    path('',views.store_product,name='store_product'),
    path('<slug:category_slug>/',views.store_product,name='product_by_category')
]
