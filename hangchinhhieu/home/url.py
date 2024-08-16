from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('base/', views.renderHome.base, name='base'),
    path('home/', views.renderHome.home, name='home'),
    path('cart/', views.renderHome.cart, name='cart'),
    path('checkouts/', views.renderHome.checkouts, name='checkouts'),
    path('account/', views.renderHome.account, name='account'),
    path('search/', views.renderHome.search, name='search'),
    path('login/', views.renderHome.Login, name='login'),

]
