from itertools import product
from django.shortcuts import get_object_or_404, render
from carts.models import CartItem
from carts.views import _cart_id
from carts.models import CartItem
from category.models import Category
from .models import Product
# Create your views here.
def store_product(request,category_slug = None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category,slug = category_slug)
        products = Product.objects.filter(category = categories,is_available = True,)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available = True)
        product_count = products.count()

    context = {
        'products' : products,
        'product_count' : product_count,

    }
    return render(request,'store_product.html',context)

def product_detail(request,category_slug,product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug,slug = product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request),product = single_product).exists() #cart__cart_id we are accessing foreign key card_id from cart

    except Exception as e:
        raise e
    context = {
        'single_product' : single_product,
        "in_cart" : in_cart,
    }
    return render(request, 'store_product/product_detail.html',context)