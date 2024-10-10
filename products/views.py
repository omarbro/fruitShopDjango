from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products=Product.objects.all()

    return render(request, 'index.html', {'prods':products})

def new_product(request):
    return HttpResponse("this the page for new product")