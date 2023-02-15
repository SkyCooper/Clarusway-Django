from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages


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

#* yeni bir todo oluşturmak/create etmek için;
#? burada serializer görevine yapacak form yapısını kullanıyoruz,
#? app içinde forms.py isimli bir dosya oluşturuyoruz.
def todo_add(request):
    # 1-context içine form'dan gelen data'yı koymak için onu bir değişkene atıyoruz,
    todo = TodoForm()
    
    if request.method == 'POST':
        
        #? request.POST ile forma girilen dataları yakalayabiliyoruz,
        print("POST :", request.POST)
        # POST : <QueryDict: {'csrfmiddlewaretoken': ['HlpQpP1ZcxD4gBSlLHo2oDAKSOY2jsVqSFeRSneCrQwWbAaRQ2TOkkAibvm7V8GB'], 'first_name': ['Kahramanmaraş'], 'last_name': ['DEPREMİ'], 'number': ['06022023'], 'image': ['']}>
        
        #? aslında image yukarıda var fakat daha kolay ulaşmak için; 
        print("FILES :", request.FILES)
        # FILES : <MultiValueDict: {'image': [<InMemoryUploadedFile: avatar-tie.png (image/png)>]}>
        
        # 2-data boş gitmemesi için içine, yukarıda örnek çıktıları verilen dataları ekliyoruz.
        todo = TodoForm(request.POST, request.FILES)
        
        # eğer gelen datalar uygunsa kayıt et.
        if todo.is_valid():
            todo.save()
            
            #? artık form sayfasında kalmasın, save olduktan sonra başka yere yönlendirilsin;
            #? redirect için url tarafında belittiğimiz ismi yazmak daha kullanışlı redirect("name")
            #? urls.py içinde name ile ilgili açıklama notu var.
            return redirect("todo_list") # name ile yazılması
            # return redirect("/list") # path ile yazılması
    
    
    # 3-değişkene atanan StudentForm()'u kullanabilmek için context içine value olarak atıyoruz,
    # context = {
    #     "todo" : todo
    # }
    
    # return render(request, "add.html", context) 
    return render(request, "add.html", {"todo" : todo})

def todo_add1(request):
    form=TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('todo_list')

    return render(request,'add.html',{'form':form})

def todo_update(request, pk):
    todo = Todo.objects.get(id=pk)
    form=TodoForm(instance=todo)
    if request.method == "POST":
        form=TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    return render(request,'update.html',{'form':form, "todo":todo})

def todo_delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('todo_list')