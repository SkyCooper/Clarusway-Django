from django.http import HttpResponse


def home(request):
  return HttpResponse('<center><h1 style="background-color:hotpink;">Welcome to Task Tracker API</h1></center>')