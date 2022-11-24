from django.shortcuts import render
from django.http import HttpResponse
from .models import Customers, Device
from django.http import JsonResponse
import json

# Create your views here.
# request -> response
# request handler
# action

customers = Customers.objects.all()

def test_page(request):
    return render(request, 'test_page.html')

def main(request):
    return render(request, 'index.html', {"customers" : customers})

def json(request):
    data = list(Device.objects.values())[-100:]
    return JsonResponse(data, safe=False)

