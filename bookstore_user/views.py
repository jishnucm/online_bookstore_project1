from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'user/user_home.html')
def books(request):
    return render(request,'user/user_books.html')
def payment(request):
    return render(request,'user/user_payment.html')
