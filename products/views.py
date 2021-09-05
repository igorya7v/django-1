from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# /products -> index
def index(request):
    return HttpResponse('Products Page')


def new(request):
    return HttpResponse('The New Products Page')
