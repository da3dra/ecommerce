"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import home_page, contact_page, login_page
from products.views import product_list_view
from carts.views import cart_home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page),
    url(r'^contact/', contact_page),
    url(r'^login/',login_page ),
    url(r'^products/',product_list_view ),
    url(r'^cart/',cart_home )
]