from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="homeadmin"),
    path('dash/', views.dashboard, name="dash"),
     path('blist/', views.booklist, name="blist"),
     path('badd/', views.bookadd, name="badd"),
      path('cat/', views.catlist, name="cat"),
       path('catadd/', views.catadd, name="catadd"),
       path('sell/', views.sellerlist, name="sell"),
      path('addsell/', views.addseller, name="addsell"),
    #    path('order2/', views.orderlist, name="order"),
        # path('order1/', views.orderdet, name="orderdet"),
]