from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('addbook/', views.addbook, name="add"),
     path('product/', views.product, name="product"),
     path('orderproduct/', views.order1, name="order"),
      path('orderdet/', views.orderdet, name="orderdet")
]