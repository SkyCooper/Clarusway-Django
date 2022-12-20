from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homefs(request):
  return HttpResponse('Hello FullStack-12')