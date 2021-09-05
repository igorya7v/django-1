from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
# /products -> index
def index(request):
    # Product.objects.filter(...)
    # Product.objects.get(...)
    # Product.objects.save(...)
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('The New Products Page')
