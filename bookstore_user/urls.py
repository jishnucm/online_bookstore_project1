from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home1"),
    path('book/', views.books, name="books"),
     path('payment/', views.payment, name="payment")
]