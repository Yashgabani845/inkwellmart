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
    path('owner/registration/', views.owner_registration_view, name='owner_registration'),
    path('add_product/', views.add_product, name='add_product'),
    path('home/search_owner/',views.search_owner,name='search_owner'),
    path('show_product/',views.show_product,name='show_product'),
    path('product_details/<str:product_name>/', views.product_details, name='product_details'),
    path('home/cat/<str:cat_name>/',views.catname),
    path('product-suggestions/', views.product_suggestions, name='product_suggestions'),
    path('profile/', views.profile, name='profile'),
    path('buy_now/<str:product_name>',views.buy_now,name='buy_now')

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
