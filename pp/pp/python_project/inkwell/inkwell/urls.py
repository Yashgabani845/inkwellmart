"""
URL configuration for stationary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from shop import views


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('home/', views.Home),
    path('',views.LoginPage),
    path('login/',views.LoginPage,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.LogoutPage,name='logout'),
    path('owner/', views.checking_owner, name='owner'),
    path('add_product/', views.add_product, name='add_product'),
    path('product_details/<str:product_name>/', views.product_details, name='product_details'),
    path('home/cat/<str:cat_name>/',views.catname, name="home/cat"),
    path('product-suggestions/', views.product_suggestions, name='product_suggestions'),
    path('profile/', views.profile, name='profile'),
    path('buy_now/<str:product_name>',views.buy_now,name='buy_now'),
    path('add-to-cart/<str:product_name>/', views.add_to_cart, name='add-to-cart'), 
    path('cart/', views.cart, name='cart'),
    path('remove/<str:product_name>/', views.remove_from_cart, name='remove'),
    path('remove/<str:product_name>/', views.remove_from_cart, name='remove_from_cart'),
    path('increase/<str:product_name>/', views.increase_quantity, name='increase_quantity'),
    path('decrease/<str:product_name>/', views.decrease_quantity, name='decrease_quantity'),
    path('owner-verification/', views.owner_verification_view, name='owner_verification'),
    path('owner-registration/', views.owner_registration_view, name='owner_registration'),
    path('owner_side',views.owner_side,name="owner_side"),
    path('buy_all/',views.buy_all,name='buy_all'),
    path('my_order/',views.my_order,name='my_order'),
    path('add_category/', views.add_category, name='add_category'),
    path('admin_side/',views.admin_side,name='admin'),
    path('all_product',views.all_product,name='all_product'),
    path('all_seller',views.all_seller,name='all_seller'),
    path('all_customer',views.all_customer,name='all_customer'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
