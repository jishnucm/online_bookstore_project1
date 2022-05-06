from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'seller/seller_home.html')
def addbook(request):
    return render(request,'seller/seller_add.html')
def product(request):
    return render(request,'seller/seller_product.html')
def order1(request):
    return render(request,'seller/seller_order1.html')
def orderdet(request):
    return render(request,'seller/seller_orderdet.html')    
