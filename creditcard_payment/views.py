from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def creditPayHome(request):
    return render(request,"billing.html" )