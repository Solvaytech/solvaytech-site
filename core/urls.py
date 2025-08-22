from django.contrib import admin
from django.urls import path, include  # add this
from .views import product_list
from ecommerce.views import checkout

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.home.urls")),             # UI Kits Html files
    path('shop/', product_list, name='product_list'),
    path('checkout/', checkout, name='checkout')
]
