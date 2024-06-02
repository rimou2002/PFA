"""
URL configuration for PFAV2 project.

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
from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('index.html/', views.index, name="index"),
    path('about.html/', views.about, name="about"),
    path('cart.html/', views.cart, name="cart"),
    path('compare.html/', views.compare, name="compare"),
    path('contacts/', views.contacts, name="contacts"),
    path('faq.html/', views.faq, name="faq"),
    path('news/', views.news, name='news'),
    path('post.html/', views.post, name="post"),
    path('product.html/', views.product, name="product"),
    path('shop.html/', views.shop, name="shop"),
    path('search_products/', views.search_products, name='search_products'),
    path('team.html/', views.team, name="team"),
    path('wishlist.html/', views.wishlist, name="wishlist"),
    path('404.html/', views.err, name="err"),
    path('registration/', views.registration, name='registration'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('login/', views.login,name='login'),
    path('managerdashboard/', views.managerdashboard, name='managerdashboard'),
    path('products/', views.product_list, name='product_list'),
    path('product.html/<int:product_id>/', views.product_detail, name='product_detail'),
    path('get_products/', views.get_products, name='get_products'),
    path('get_products_by_effect/', views.get_products_by_effect, name='get_products_by_effect'),
    path('chat/', include('chatbot.urls')),  # Inclusion des URLs de l'application chatbot
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),

    #path('product/<int:product_id>/', views.product, name="product"),
    #path('product_detail/', views.product_detail, name='product_detail'),
    path('', include('myapp.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)