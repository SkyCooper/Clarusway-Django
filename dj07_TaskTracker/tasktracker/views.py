from django.shortcuts import render, get_object_or_404

#? FUNCTION VIEW
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#? CONCRETE VIEWS
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

#? VIEWSETS
from rest_framework.viewsets import ModelViewSet

#? MY IMPORTS
from .models import Todo
from .serializer import TodoSerializer

# Create your views here.
@api_view()
def todo_home(request):
  return Response({"home" : "this is todo home"})

#* ==========================================================
#TODO,         FUNCTION BASED VİEWS
#* ==========================================================

#! ==========================================================
#! pk istemeyenler için bir tane fonksiyon yazıp birleştirilebilir.
#! ==========================================================
@api_view(['GET', 'POST'])
def todo_list_create(request):
  if request.method == 'GET':
    # todos = Todo.objects.all() #? Tamamı
    todos = Todo.objects.filter(is_done=False) #? Tamamlanmamış olanlar
    serializer = TodoSerializer(todos, many=True) #? many=True queryset olduğundan
    return Response(serializer.data)
  
  if request.method == 'POST':
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#! ==========================================================
#! pk, İSTEYENLER için birtane fonksiyon yazıp birleştirilebilir.
#! ==========================================================
@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, pk):
  todo =  get_object_or_404(Todo,id=pk)
  
  if request.method == 'GET':
    # todo = Todo.objects.get(id=pk) #? yanlış id gelirse hata verir.
    # todo =  get_object_or_404(Todo,id=pk) #? hepsinde ortak olduğundan en üste aldık.
    serializer = TodoSerializer(todo) #? many=True gerek yok queryset olmadığı için
    return Response(serializer.data)
  
  if request.method == 'PUT':
    serializer = TodoSerializer(data=request.data, instance=todo)
    # serializer = TodoSerializer(todo, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
  
  if request.method == 'DELETE':
    todo.delete()
    return Response({'message': 'todo deleted succesfully'})
  


#* ==========================================================
#TODO                     CLASS BASED VİEWS
#* ==========================================================

#? ==========================================================
#? CONCRETE VIEWS  --  çok sık kullanılan yöntem
#? ==========================================================

#! pk istemeyenler için bir tane fonksiyon
class Todos(ListCreateAPIView):
  queryset = Todo.objects.filter(is_done=False)
  serializer_class = TodoSerializer  

#! pk GEREKLİ OLANLAR için bir tane fonksiyon   
class TodoDetail(RetrieveUpdateDestroyAPIView):
  queryset = Todo.objects.filter(is_done=False)
  serializer_class = TodoSerializer
  
  # eğer urls.py de pk yerine id yazılmış ise burada lookup_field tanımlanmalı
  # lookup_field = 'id'
  
#? ==========================================================
#? VIEWSETS
#? ==========================================================

#! Tek bir view oluşturarak hem pk/id (lookup) gerekli olmayan,(GET, POST)
#! Hem de pk/id (lookup) isteyen bütün bütün işlemleri yapabiliyoruz. (GET, PUT, PATCH, DELETE)
  
class TodoMVS(ModelViewSet):
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer  
  
  
  
  
  
  
  
  
  
  