from django.shortcuts import render

# Create your views here.
from .models import Product

def product_list_view(request):
    queryset = Product.objects.all()
    context={
        'object_list':queryset
    }
    return render(request,"products/list.html",context )

