from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def real_home(request):
  return HttpResponse(" Welcome my Real Home...")