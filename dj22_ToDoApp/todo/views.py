from django.shortcuts import render
from .models import Todo
from .forms import TodoForm

# Create your views here.
def todo_list(request):
    #? bütün todo'ları görüntüleyebilmek için
    #? Todo modeldeki bütün objeleri alıp değişkene atadık,
    todos = Todo.objects.all()
    #? gelen data bir queryset'tir.
    
    #? bu student değişkeni context içinde value olacak şekilde yeniden tanımladık,
    context = {
        "todos" : todos
    }
    
    #? ve context içindeki herşeyi kullanabilmek için list.html içine aktardık.
    return render(request, "list.html", context)    