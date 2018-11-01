from django.db import models
from django.conf import settings
from products.models import Product

User = settings.AUTH_USER_MODEL


class CartManager(models.Manager):
    def new_or_get(self,request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            print("Cart exists")
            cart = qs.first()
            if request.user.is_authenticated() and cart.user is None:
                cart.user = request.user
                cart.save()
        else:
            new_obj = True
            cart = self.new_cart(user=None)
            request.session['cart_id'] = cart.id
        return cart, new_obj

    def new_cart(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated():
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)
    objects = CartManager()

    def __str__(self):
        return str(self.id)

