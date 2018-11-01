from django.shortcuts import render
from .models import Cart
# Create your views here.

def cart_home(request):
    cart = Cart.objects.new_or_get(request)
    return render(request, "carts/cart.html", {})

