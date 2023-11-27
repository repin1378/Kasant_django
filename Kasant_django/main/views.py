from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h4>Hello world!</h4>")

def about(request):
    return HttpResponse("<h8>О программе</h8>")
