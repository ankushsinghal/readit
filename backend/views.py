from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def say_hello(request):
    context = {}
    return HttpResponse('Hello Ankush!')

def go_to_home(request):
    context = {}
    return render(request, 'index.html', context)